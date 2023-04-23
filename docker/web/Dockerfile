FROM node:18 as DIST
WORKDIR /web
COPY web .
RUN npm install --registry=https://registry.npmmirror.com -g pnpm \
    && pnpm install --registry=https://registry.npmmirror.com \
    && cp .env.docker .env.production \
    && pnpm build

FROM nginx:alpine
COPY ./docker/web/nginx.conf /etc/nginx/conf.d/fuadmin.conf
COPY --from=DIST /web/dist /usr/share/nginx/html

