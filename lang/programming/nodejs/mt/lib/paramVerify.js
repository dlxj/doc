/**
 * 参数验证
 * @returns params 
 */
module.exports = function (paramsDefined, body) {
  const newParams = {};
  if (paramsDefined === null || paramsDefined === undefined) {
    return newParams;
  }
  for (const key in paramsDefined) {
    const p = paramsDefined[key];
    if (p.default !== undefined) {
      if (body[key] == undefined || body[key] == null) {
        newParams[key] = p.default;
        continue
      } else {
        newParams[key] = body[key]
      }
    } else {
      if (body[key] === undefined || body[key] === '') {
        throw new Error(`参数${key}不能为空！`);
      }
    }
    if (p.maxLen != undefined && p['type'].toLowerCase() !== 'array') {
      if (body[key] !== undefined && body[key].length > p.maxLen) {
        throw new Error(`系统错误,${key}过长！`);
      }
    }
    switch (p['type'].toLowerCase()) {
      case "string":
        newParams[key] = `${body[key]}`;
        break;
      case "enum":
        if (p.range === null || p.range === undefined || p.range.includes === undefined) {
          throw new Error(`系统错误,${key}未设定枚举值！`);
        }
        if (!p.range.includes(body[key])) {
          throw new Error(`参数${key}不正确！`);
        }
        newParams[key] = body[key];
        break;
      case "array":
        try {

          let data = body[key];
          if (!Array.isArray(data)) {
            data = JSON.parse(data);
          }

          if (!Array.isArray(data)) {
            throw new Error(`参数${key}不是数组！`);
          }
          if (p.maxLen !== undefined && data.length > p.maxLen) {
            throw new Error(`参数${key}长度溢出！`);
          }
          newParams[key] = data;
        } catch (ex) {
          throw new Error(`参数${key}不是数组！`);
        }
        break;
      case "json":
        try {
          let data1 = body[key];
          if (typeof (data1) !== 'object') {
            data1 = JSON.parse(data1);
          }

          if (typeof (data1) !== 'object') {
            throw new Error(`参数${key}无法正常转化为json！`);
          }
          newParams[key] = data1;
        } catch (ex) {
          throw new Error(`参数${key}无法正常转化为json！`);
        }
        break;
      case "bool":
        const data2 = body[key] === 'true' || body[key] === true ? true : body[key] === 'false' || body[key] === false ? false : '';
        if (data2 !== 'true' && data2 !== 'false' && data2 !== true && data2 !== false) {
          throw new Error(`参数${key}不正确！`);
        }
        newParams[key] = data2;
        break;
      case "regex":
        const r = new RegExp(p.explain);
        if (typeof (r.test) !== 'function') {
          throw new Error(`系统错误，${key}未设定正则表达式！`);
        }
        if (r.test(body[key]) !== true) {
          throw new Error(`参数${key}不正确！`);
        }
        newParams[key] = body[key];
        break;
      case 'number':
        if (typeof (Number(body[key])) !== 'number') {
          throw new Error(`参数${key}值不正确！`);
        }
        newParams[key] = Number(body[key]);
        break;
      case 'date':
        var reDate = /^(?:19|20)[0-9][0-9]-(?:(?:0[1-9])|(?:1[0-2]))-(?:(?:[0-2][1-9])|(?:[1-3][0-1]))$/;
        if (!reDate.test(body[key])) {
          throw new Error(`参数${key}日期格式不正确`);
        }
        break;
      case 'datetime':
        var reDate = /^(?:19|20)[0-9][0-9]-(?:(?:0[1-9])|(?:1[0-2]))-(?:(?:[0-2][1-9])|(?:[1-3][0-1])) (?:(?:[0-2][0-3])|(?:[0-1][0-9])):[0-5][0-9]:[0-5][0-9]$/;
        if (!reDate.test(body[key])) {
          throw new Error(`参数${key}时间格式不正确`);
        }
      default:
        throw new Error(`未知参数类型${p['type']}`);
    }
  }
  return newParams;
}