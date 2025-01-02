FROM node:16 as builder

WORKDIR /app

# Copy all files to the working directory
COPY ./ ./

# Install dependencies and build the application
RUN yarn add axios
RUN yarn install
RUN yarn build

FROM nginx:alpine3.18 as production-stage

# Create the /app directory
RUN mkdir /app

COPY --from=builder /app/dist /app
EXPOSE 80
COPY nginx.conf /etc/nginx/nginx.conf