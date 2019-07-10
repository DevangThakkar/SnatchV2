// Setup basic express server
var express = require("express");
var app = express();
var path = require("path");
var server = require("http").createServer(app);
var io = require("socket.io")(server);
var port = process.env.PORT || 3000;
var PythonShell = require("python-shell");

server.listen(port, () => {
  console.log('Server listening at port %d', port);
});

// Routing
app.use(express.static(path.join(__dirname, "public")));

// Chatroom
var numUsers = 0;

var centre = " Centre: ";
// Yes, I have removed the blanks because I was lazy; you may add them
var bag = "EEIBOOLEHALAPYTERWJRANEOSIDRRFLOESETAMQGIUVIUBPIKIFATRGNIADESTANHIDMGNEXTUOCRETLOISAZOYUODCNVNEAWE";
var bag_og = bag;
var words = new Object();
words['the_void\u2122'] = [];

var active1 = true;
var active2 = false;

io.on("connection", (socket) => {
	var addedUser = false;
	// setInterval(() => {
	//     io.emit('new message', {
	//     	username: "snatch-daemon",
	// 		message: "just keeping this server awake, please continue"
	//     });
	// }, 1200000);

	// when the client emits "new message", this listens and executes
	socket.on("new message", (data) => {
		// we tell the client to execute "new message"
		socket.broadcast.emit("new message", {
			username: socket.username,
			message: data
		});

		// while (active1 && active2){}

		active1 = true;
		active2 = true;

		var options_c = {
			mode: "text",
			args: [centre.substring(8), data, socket.username.toLowerCase(), JSON.stringify(words)]
		};
		PythonShell.run("check.py", options_c, function (err, results) {
			if (err){
				throw err;
			}
			// results is an array of messages collected during execution
			console.log("results: %j", results);

			// if an invalid word is made
			if (parseInt(results[0]) == -1){
				centre = results[2];
				io.emit("new message", {
					username: "snatch",
					message: results[1]+results[2]
				});
				var str = "";
				for(var key in words){
					if (words[key].length>0) {
						str += key + ": " + words[key] + "; ";
					}
				}
				io.emit("new message", {
					username: "snatch",
					message: str
				});
				active1 = false;
			}
			// if a valid word is made
			if (parseInt(results[0]) == 1){
				centre = results[2];
				word = results[1].substring(results[1].indexOf(":") + 2);
				word = word.replace(", ", "");
				words[socket.username].push(word);
				console.log(words);
				io.emit("new message", {
					username: "snatch",
					message: results[1] + results[2]
				});
				var str = ""
				for(var key in words){
					if (words[key].length>0) {
						str += key + ": " + words[key] + "; ";
					}
				}
				io.emit("new message", {
					username: "snatch",
					message: str
				});
				active1 = false;
			}
			// if valid tiles are drawn
			if (parseInt(results[0]) == 2){
				var options_d = {
					mode: "text",
					args: [centre.substring(8), bag, results[1], socket.username.toLowerCase()]
				}
				PythonShell.run("draw.py", options_d, function(err, results) {
					if (err) throw err;
					// results is an array of messages collected during execution
					console.log("results_d: %j", results);

					if (parseInt(results[0]) == 0){
						io.emit("new message", {
							username: "snatch",
							message: results[1] + results[2]
						});
						var str = ""
						for(var key in words){
							if (words[key].length>0) {
								str += key + ": " + words[key] + "; ";
							}
						}
						io.emit("new message", {
							username: "snatch",
							message: str
						});
						active1 = false;
					}

					if (parseInt(results[0]) == 1){
						centre = results[2]
						io.emit("new message", {
							username: "snatch",
							message: results[1] + results[2]
						});
						var str = ""
						for(var key in words){
							if (words[key].length>0) {
								str += key + ": " + words[key] + "; ";
							}
						}
						io.emit("new message", {
							username: "snatch",
							message: str
						});
						bag = results[3]
						active1 = false;
					}
				});
			}

			if(parseInt(results[0]) == -2){
				io.emit("new message", {
					username: "snatch",
					message: results[1] + results[2]
				});
				var str = ""
				for(var key in words){
					if (words[key].length>0) {
						str += key + ": " + words[key] + "; ";
					}
				}
				io.emit("new message", {
					username: "snatch",
					message: str
				});
				active1 = false;
			}

			if(parseInt(results[0]) == 0){
				active1 = false;
			}

			if(parseInt(results[0]) == 3){
				centre = results[2]
				io.emit("new message", {
					username: "snatch",
					message: results[1] + results[2]
				});
				temp = words[results[3]]
				temp.splice(temp.indexOf(results[4]), 1)
				words[results[3]] = temp
				var str = ""
				for(var key in words){
					if (words[key].length>0) {
						str += key + ": " + words[key] + "; ";
					}
				}
				io.emit("new message", {
					username: "snatch",
					message: str
				});
				active1 = false;
			}

			if(parseInt(results[0]) == -3){
				io.emit("new message", {
					username: "snatch",
					message: results[1] + results[2]
				});
				var str = ""
				for(var key in words){
					if (words[key].length>0) {
						str += key + ": " + words[key] + "; ";
					}
				}
				io.emit("new message", {
					username: "snatch",
					message: str
				});
				active1 = false;
			}

			if(parseInt(results[0]) == 4){
				centre = results[2]
				io.emit("new message", {
					username: "snatch",
					message: results[1] + results[2]
				});
				console.log(results[1])
				words[socket.username].push(results[5]);
				temp = words[results[3]]
				console.log(results[3])
				console.log(word[results[3]])
				temp.splice(temp.indexOf(results[4]), 1)
				words[results[3]] = temp
				var str = ""
				for(var key in words){
					if (words[key].length>0) {
						str += key + ": " + words[key] + "; ";
					}
				}
				io.emit("new message", {
					username: "snatch",
					message: str
				});
				active1 = false;
			}

			if(parseInt(results[0]) == -9){
				centre = results[2]
				io.emit("new message", {
					username: "snatch",
					message: results[1] + results[2]
				});
				bag = bag_og
				var str = ""
				for(var key in words){
					words[key] = []
					if (words[key].length>0) {
						str += key + ": " + words[key] + "; ";
					}
				}
				io.emit("new message", {
					username: "snatch",
					message: str
				});
				active1 = false;
			}

		});
	});

	// when the client emits "add user", this listens and executes
	socket.on("add user", (username) => {
		if (addedUser)
			return;

		temp_username = '';
		for (var i = 0, n = username.length; i < n; i++) {
			if (username.charCodeAt( i ) < 255) { 
				temp_username = temp_username + username[i];
			}
		}
		username = temp_username;
		console.log('hello');
		for(var key in words){
			console.log(key);
		}
		console.log('hello');
		if (username.toLowerCase() in words){
			console.log(username);
			console.log(words[username]);
			console.log('duplicate');
			username = username + Math.floor(Math.random() * 1000);
		}
		console.log(username);
		console.log(socket.username);
		words[username.toLowerCase()] = []

		// we store the username in the socket session for this client
		socket.username = username;
		++numUsers;
		addedUser = true;
		socket.emit("login", {
			numUsers: numUsers
		});
		// echo globally (all clients) that a person has connected
		socket.broadcast.emit("user joined", {
			username: socket.username,
			numUsers: numUsers
		});
	});

	// when the client emits "typing", we broadcast it to others
	socket.on("typing", () => {
		socket.broadcast.emit("typing", {
			username: socket.username
		});
	});

	// when the client emits "stop typing", we broadcast it to others
	socket.on("stop typing", () => {
		socket.broadcast.emit("stop typing", {
			username: socket.username
		});
	});

	// when the user disconnects.. perform this
	socket.on("disconnect", () => {
		if (addedUser) {
			--numUsers;

			words['the_void\u2122'] = words['the_void\u2122'].concat(words[socket.username])
			words[socket.username] = []

			// echo globally that this client has left
			socket.broadcast.emit("user left", {
				username: socket.username,
				numUsers: numUsers
			});
		}
	});
});