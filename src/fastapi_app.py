import logging
from fastapi import FastAPI, Request
from telegram import Update
from . import app_config
from .telegram import create_bot_application
from .ml_module import start_up_ml


application = create_bot_application()
print('1')
start_up_ml()
print('2')
def create_fastapi_app():
    app = FastAPI()
    @app.post(f"/{app_config.TELEGRAM_BOT_TOKEN}/webhook")
    async def telegram_webhook(request: Request):
        """Webhook endpoint to receive updates from Telegram."""
        update = Update.de_json(await request.json(), application.bot)
        await application.process_update(update)
        return {"ok": True}

    
    @app.on_event("startup")
    async def on_startup():
        """Initialize and start the bot application."""
        await application.initialize()
        print('3')
        await application.start()
        print('4')
        await application.updater.start_polling()
        print('5')

        
    @app.on_event("shutdown")
    async def on_shutdown():
        """Shutdown the bot application."""
        await application.shutdown()
        await application.stop()

    return app