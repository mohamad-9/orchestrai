FROM node:20

WORKDIR /app

# Copy everything
COPY . .

# Clean install (important for Docker)
RUN rm -rf node_modules package-lock.json
RUN npm install

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]