FROM node:lts-alpine

RUN yarn global add @vue/cli

ADD . /frontend

CMD ["vue", "ui", "--headless", "--port" , "8000", "--host", "0.0.0.0"]