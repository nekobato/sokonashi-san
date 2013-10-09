
#
# * GET home page.
#
exports.index = (req, res) ->
  res.render "index",
    title: "Express"

exports.timeline = (req, res) ->
  db = module.parent.exports.mongoose

  Sokonashi = db.model('user')
  Sokonashi.find {}, (err, docs) ->
    for doc in docs
      console.log(doc)

  res.render "timeline",
    title: "Express"
