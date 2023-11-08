# 🌙 Illuasion

Do this in this order:

```bash
git clone git@github.com:michaljanocko/illuasion.git
cd illuasion
docker build -t illuasion
```

and run the Docker container. (Don't forget to bind the port **80**)

Then just send a `POST` request to `/` with form-encoded Lua bytecode
in the `bytecode` field.

That's it. Enjoy! _mic drop_
