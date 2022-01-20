import {execa} from 'execa';
const {stdout} = await execa('dir', []);
console.log(stdout);
console.log(111)