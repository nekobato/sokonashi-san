###
Module dependencies.
###
express = require("express")
routes = require("./routes")
http = require("http")
path = require("path")
mongoose = module.exports.mongoose = require("mongoose")
app = express()


# all environments
app.set "port", process.env.PORT or 3000
app.set "views", __dirname + "/views"
app.set "view engine", "jade"
app.use express.favicon()
app.use express.logger("dev")
app.use express.bodyParser()
app.use express.methodOverride()
app.use app.router
app.use require("stylus").middleware(__dirname + "/public")
app.use express.static(path.join(__dirname, "public"))

#mongoose
app.set "mongoose", mongoose
Schema = mongoose.Schema;
UserSchema = new Schema {}
mongoose.model('user', UserSchema);
mongoose.connect('mongodb://nekobato.net/sokonashi')

# development only
app.use express.errorHandler() if "development" is app.get("env")
app.get "/", routes.index

app.get "/timeline", routes.timeline

http.createServer(app).listen app.get("port"), ->
  console.log "Express server listening on port " + app.get("port")