'use strict'

const genfun = require('./generate-function')
const { buildSchemas } = require('./pointer')
const { compile } = require('./compile')
const functions = require('./scope-functions')

const validator = (schema, { jsonCheck = false, isJSON = false, schemas, ...opts } = {}) => {
  if (jsonCheck && isJSON) throw new Error('Can not specify both isJSON and jsonCheck options')
  const options = { ...opts, schemas: buildSchemas(schemas || []), isJSON: isJSON || jsonCheck }
  const { scope, ref } = compile(schema, options)
  if (opts.dryRun) return
  const fun = genfun()
  if (!jsonCheck || opts.dryRun) {
    fun.write('%s', ref)
  } else {
    // jsonCheck wrapper implementation below
    scope.deepEqual = functions.deepEqual
    fun.write('function validateIsJSON(data) {')
    if (opts.includeErrors) {
      fun.write('if (!deepEqual(data, JSON.parse(JSON.stringify(data)))) {')
      fun.write('validateIsJSON.errors = [{instanceLocation:"#",error:"not JSON compatible"}]')
      fun.write('return false')
      fun.write('}')
      fun.write('const res = %s(data)', ref)
      fun.write('validateIsJSON.errors = actualValidate.errors')
      fun.write('return res')
    } else {
      fun.write('return deepEqual(data, JSON.parse(JSON.stringify(data))) && %s(data)', ref)
    }
    fun.write('}')
  }
  const validate = fun.makeFunction(scope)
  validate.toModule = () => fun.makeModule(scope)
  validate.toJSON = () => schema
  return validate
}

const parser = function(schema, opts = {}) {
  // strong mode is default in parser
  if (functions.hasOwn(opts, 'jsonCheck') || functions.hasOwn(opts, 'isJSON'))
    throw new Error('jsonCheck and isJSON options are not applicable in parser mode')
  const validate = validator(schema, { mode: 'strong', ...opts, jsonCheck: false, isJSON: true })
  const parse = opts.includeErrors
    ? (src) => {
        if (typeof src !== 'string') return { valid: false, error: 'Input is not a string' }
        try {
          const value = JSON.parse(src)
          if (!validate(value)) {
            const { keywordLocation, instanceLocation } = validate.errors[0]
            const keyword = keywordLocation.slice(keywordLocation.lastIndexOf('/') + 1)
            const error = `JSON validation failed for ${keyword} at ${instanceLocation}`
            return { valid: false, error, errors: validate.errors }
          }
          return { valid: true, value }
        } catch ({ message }) {
          return { valid: false, error: message }
        }
      }
    : (src) => {
        if (typeof src !== 'string') return { valid: false }
        try {
          const value = JSON.parse(src)
          if (!validate(value)) return { valid: false }
          return { valid: true, value }
        } catch (e) {
          return { valid: false }
        }
      }
  parse.toModule = () =>
    [
      '(function(src) {',
      `const validate = ${validate.toModule()}`,
      `const parse = ${parse}\n`,
      'return parse(src)',
      '});',
    ].join('\n')
  parse.toJSON = () => schema
  return parse
}

module.exports = { validator, parser }
