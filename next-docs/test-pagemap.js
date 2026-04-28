const fs = require('fs');
const html = fs.readFileSync('.next/server/app/01-python.html', 'utf8');
const idx = html.indexOf('"pageMap":[');
if (idx > -1) {
  let depth = 0;
  let end = idx + 10;
  for (let i = end; i < html.length; i++) {
    if (html[i] === '[') depth++;
    if (html[i] === ']') {
      if (depth === 0) { end = i + 1; break; }
      depth--;
    }
  }
  const jsonStr = html.substring(idx + 10, end);
  fs.writeFileSync('pageMap.json', jsonStr);
  const data = JSON.parse(jsonStr);
  console.log("length:", data.length);
  console.log("first item:", Object.keys(data[0]), data[0].name);
  fs.writeFileSync('pageMap-sample.json', JSON.stringify(data.slice(0,2), null, 2));
}
