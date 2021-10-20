'use strict'

const { knownKeywords } = require('./known-keywords')

function untilde(string) {
  if (!string.includes('~')) return string
  return string.replace(/~[01]/g, (match) => {
    switch (match) {
      case '~1':
        return '/'
      case '~0':
        return '~'
    }
    /* c8 ignore next */
    throw new Error('Unreachable')
  })
}

function get(obj, pointer, objpath) {
  if (typeof obj !== 'object') throw new Error('Invalid input object')
  if (typeof pointer !== 'string') throw new Error('Invalid JSON pointer')
  const parts = pointer.split('/')
  if (!['', '#'].includes(parts.shift())) throw new Error('Invalid JSON pointer')
  if (parts.length === 0) return obj

  let curr = obj
  for (const part of parts) {
    if (typeof part !== 'string') throw new Error('Invalid JSON pointer')
    if (objpath) objpath.push(curr) // does not include target itself, but includes head
    const prop = untilde(part)
    if (typeof curr !== 'object') return undefined
    if (!Object.prototype.hasOwnProperty.call(curr, prop)) return undefined
    curr = curr[prop]
  }
  return curr
}

const protocolRegex = /^https?:\/\//

function joinPath(baseFull, sub) {
  if (typeof baseFull !== 'string' || typeof sub !== 'string') throw new Error('Unexpected path!')
  if (sub.length === 0) return baseFull
  const base = baseFull.replace(/#.*/, '')
  if (sub.startsWith('#')) return `${base}${sub}`
  if (!base.includes('/') || protocolRegex.test(sub)) return sub
  if (protocolRegex.test(base)) return `${new URL(sub, base)}`
  if (sub.startsWith('/')) return sub
  return [...base.split('/').slice(0, -1), sub].join('/')
}

function objpath2path(objpath) {
  const ids = objpath.map((obj) => (obj && (obj.$id || obj.id)) || '')
  return ids.filter((id) => id && typeof id === 'string').reduce(joinPath, '')
}

const withSpecialChilds = ['properties', 'patternProperties', '$defs', 'definitions']

// Returns a list of resolved entries, in a form: [schema, root, basePath]
// basePath doesn't contain the target object $id itself
function resolveReference(root, additionalSchemas, ref, base = '') {
  const ptr = joinPath(base, ref)
  const schemas = new Map(additionalSchemas)
  const self = (base || '').split('#')[0]
  if (self) schemas.set(self, root)

  const results = []

  const [main, hash = ''] = ptr.split('#')
  const local = decodeURI(hash).replace(/\/$/, '')

  // Find in self by id path
  const visit = (sub, oldPath, specialChilds = false, dynamic = false) => {
    if (!sub || typeof sub !== 'object') return
    const id = sub.$id || sub.id
    let path = oldPath
    if (id && typeof id === 'string') {
      path = joinPath(path, id)
      if (path === ptr || (path === main && local === '')) {
        results.push([sub, root, oldPath])
      } else if (path === main && local[0] === '/') {
        const objpath = []
        const res = get(sub, local, objpath)
        if (res !== undefined) results.push([res, root, joinPath(oldPath, objpath2path(objpath))])
      }
    }
    const anchor = dynamic ? sub.$dynamicAnchor : sub.$anchor
    if (anchor && typeof anchor === 'string') {
      if (anchor.includes('#')) throw new Error("$anchor can't include '#'")
      if (anchor.startsWith('/')) throw new Error("$anchor can't start with '/'")
      path = joinPath(path, `#${anchor}`)
      if (path === ptr) results.push([sub, root, oldPath])
    }
    for (const k of Object.keys(sub)) {
      if (!specialChilds && !Array.isArray(sub) && !knownKeywords.includes(k)) continue
      if (!specialChilds && ['const', 'enum', 'examples', 'comment'].includes(k)) continue
      visit(sub[k], path, !specialChilds && withSpecialChilds.includes(k))
    }
    if (!dynamic && sub.$dynamicAnchor) visit(sub, oldPath, specialChilds, true)
  }
  visit(root, '')

  // Find in self by pointer
  if (main === '' && (local[0] === '/' || local === '')) {
    const objpath = []
    const res = get(root, local, objpath)
    if (res !== undefined) results.push([res, root, objpath2path(objpath)])
  }

  // Find in additional schemas
  if (schemas.has(main)) {
    const additional = resolveReference(schemas.get(main), additionalSchemas, `#${hash}`)
    results.push(...additional.map(([res, rRoot, rPath]) => [res, rRoot, joinPath(main, rPath)]))
  }

  // Full refs to additional schemas
  if (schemas.has(ptr)) results.push([schemas.get(ptr), schemas.get(ptr), ptr])

  return results
}

function getDynamicAnchors(schema) {
  const results = new Map()
  const visit = (sub, specialChilds = false) => {
    if (!sub || typeof sub !== 'object') return
    if (sub !== schema && (sub.$id || sub.id)) return // base changed, no longer in the same resource
    const anchor = sub.$dynamicAnchor
    if (anchor && typeof anchor === 'string') {
      if (anchor.includes('#')) throw new Error("$dynamicAnchor can't include '#'")
      if (!/^[a-zA-Z0-9_-]+$/.test(anchor)) throw new Error(`Unsupported $dynamicAnchor: ${anchor}`)
      if (results.has(anchor)) throw new Error(`duplicate $dynamicAnchor: ${anchor}`)
      results.set(anchor, sub)
    }
    for (const k of Object.keys(sub)) {
      if (!specialChilds && !Array.isArray(sub) && !knownKeywords.includes(k)) continue
      if (!specialChilds && ['const', 'enum', 'examples', 'comment'].includes(k)) continue
      visit(sub[k], !specialChilds && withSpecialChilds.includes(k))
    }
  }
  visit(schema)
  return results
}

function hasKeywords(schema, keywords) {
  const visit = (sub, specialChilds = false) => {
    if (!sub || typeof sub !== 'object') return false
    for (const k of Object.keys(sub)) {
      if (keywords.includes(k)) return true
      if (!specialChilds && !Array.isArray(sub) && !knownKeywords.includes(k)) continue
      if (!specialChilds && ['const', 'enum', 'examples', 'comment'].includes(k)) continue
      if (visit(sub[k], !specialChilds && withSpecialChilds.includes(k))) return true
    }
    return false
  }
  return visit(schema)
}

const buildSchemas = (input) => {
  if (input) {
    switch (Object.getPrototypeOf(input)) {
      case Object.prototype:
        return new Map(Object.entries(input))
      case Map.prototype:
        return new Map(input)
      case Array.prototype: {
        // In this case, schema ids are extracted from the schemas themselves
        const schemas = new Map()
        const cleanId = (id) =>
          // # is allowed only as the last symbol here
          id && typeof id === 'string' && !/#./.test(id) ? id.replace(/#$/, '') : null
        for (const schema of input) {
          const visit = (sub) => {
            if (!sub || typeof sub !== 'object') return
            const id = cleanId(sub.$id || sub.id)
            if (id && id.includes('://')) {
              if (schemas.has(id)) throw new Error("Duplicate schema $id in 'schemas'")
              schemas.set(id, sub)
            } else if (sub === schema) {
              throw new Error("Schema with missing or invalid $id in 'schemas'")
            }
            for (const k of Object.keys(sub)) visit(sub[k])
          }
          visit(schema)
        }
        return schemas
      }
    }
  }
  throw new Error("Unexpected value for 'schemas' option")
}

module.exports = { get, joinPath, resolveReference, getDynamicAnchors, hasKeywords, buildSchemas }
