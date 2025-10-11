# Build stage
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build  # outputs HTML files into /app/dist

# Runtime stage
FROM nginx:1.27-alpine
RUN rm -f /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/site.conf
EXPOSE 80
