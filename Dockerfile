FROM node:16 as builder

WORKDIR /app

COPY /package.json /yarn.lock ./
COPY ./ ./
RUN yarn add axios
RUN yarn install
RUN yarn build

FROM nginx:alpine3.18 as production-stage
RUN mkdir /app
COPY --from=builder /app/dist /app
EXPOSE 80
COPY nginx.conf /etc/nginx/nginx.conf