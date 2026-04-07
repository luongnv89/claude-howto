# Stage 1: Build
FROM node:20-alpine AS builder

# Install git for lastUpdated feature
RUN apk add --no-cache git

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --prefer-offline

# Copy source files
COPY . .

# Build documentation
RUN npm run docs:build

# Stage 2: Production
FROM nginx:alpine

# Copy built files to nginx
COPY --from=builder /app/.vitepress/dist /usr/share/nginx/html

# Convert README.html to index.html in all directories (VitePress convention)
RUN find /usr/share/nginx/html -name "README.html" -exec sh -c 'cp "$1" "${1%/*}/index.html"' _ {} \;

# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]