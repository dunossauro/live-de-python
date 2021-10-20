import { traverse } from '../traverse';
export function sampleObject(schema, options = {}, spec, context) {
  let res = {};
  const depth = (context && context.depth || 1);

  if (schema && typeof schema.properties === 'object') {
    let requiredKeys = (Array.isArray(schema.required) ? schema.required : []);
    let requiredKeyDict = requiredKeys.reduce((dict, key) => {
      dict[key] = true;
      return dict;
    }, {});

    Object.keys(schema.properties).forEach(propertyName => {
      // skip before traverse that could be costly
      if (options.skipNonRequired && !requiredKeyDict.hasOwnProperty(propertyName)) {
        return;
      }

      const sample = traverse(schema.properties[propertyName], options, spec, { propertyName, depth: depth + 1 });
      if (options.skipReadOnly && sample.readOnly) {
        return;
      }

      if (options.skipWriteOnly && sample.writeOnly) {
        return;
      }
      res[propertyName] = sample.value;
    });
  }

  if (schema && typeof schema.additionalProperties === 'object') {
    res.property1 = traverse(schema.additionalProperties, options, spec, {depth: depth + 1 }).value;
    res.property2 = traverse(schema.additionalProperties, options, spec, {depth: depth + 1 }).value;
  }
  return res;
}
