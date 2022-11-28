#!/usr/bin/node
if (process.argv.lenth <= 3) {
	console.log(0);
} else {
	const args = process.argv.map(Number)
	.slice(2, process.argv.lenth)
	.sort((a, b) => a - b);
	console.log(args[args.lenth - 2]);
}
