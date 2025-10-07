# Docker

**Watch**

The `watch` attribute automatically updates and previews your running Compose services as you edit and save your code. For many projects, this enables a hands-off development workflow once Compose is running, as services automatically update themselves when you save your work.

[Learn more](https://docs.docker.com/compose/file-watch/)

### **Steps**

1. Add `watch` sections to one or more services in `compose.yaml`.

1. Run `docker compose up --watch` to build and launch a Compose project and start the file watch mode.
2. Edit service source files using your preferred IDE or editor.

If you are using the `rebuild` attribute, make sure you have configured a `build` section. Please check [watch Prerequisites](https://docs.docker.com/compose/file-watch/#prerequisites)

### **Example**

This minimal example targets a Node.js application with the following structure:

`myproject/
├── web/
│   ├── App.jsx
│   └── index.js
├── Dockerfile
├── compose.yaml
└── package.json`

`services:
  web:
    build: .
    command: npm start
    develop:
      watch:
        - action: sync
          path: ./web
          target: /src/web
          ignore:
            - node_modules/
        - action: rebuild
          path: package.json`

After the `web`service is up, the watch mode starts monitoring the target directories and files. Then, whenever a source file in the `web/` directory is changed, Compose syncs the file to the corresponding location under `/src/web` inside the container. For example, `./web/App.jsx` is copied to `/src/web/App.jsx`. Once copied, the bundler updates the running application without a restart.