FROM node:18 as DIST
WORKDIR /go-view
COPY web .
RUN npm install --registry=https://registry.npmmirror.com -g pnpm \
    && pnpm install --registry=https://registry.npmmirror.com \
    && cp .env.docker .env \
    && pnpm build

FROM nginx:alpine
COPY ./docker/go-view/nginx.conf /etc/nginx/conf.d/fuadmin.conf
COPY --from=DIST /go-view/dist /usr/share/nginx/html

