FROM node:16 as builder

WORKDIR /app

COPY /package.json /yarn.lock ./
COPY ./ ./
# RUN yarn add axios
# RUN yarn global add @vue/cli
RUN npm install
RUN npm run dev

FROM nginx:alpine3.18 as production-stage
RUN mkdir /app
COPY --from=builder /app/dist /app
EXPOSE 80
COPY nginx.conf /etc/nginx/nginx.conf

# FROM nginx:1.21-alpine
# COPY --from=builder /app/dist /usr/share/nginx/html/