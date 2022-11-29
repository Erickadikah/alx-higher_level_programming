#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let x = searchElement
	let n = list.length
        let res = 0;
        for (let i=0; i<n; i++)
        {
            if (x == list[i])
                res++;
        }
        return res;
    }
