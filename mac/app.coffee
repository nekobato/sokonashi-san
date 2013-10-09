exec = require('child_process').exec

console.log 'detecting...'
exec 'python sokonashi.py', (err, stdout, stderr) ->
	console.log stdout
