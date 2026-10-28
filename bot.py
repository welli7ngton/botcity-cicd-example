from botcity.web import WebBot, Browser, By
from botcity.maestro import BotMaestroSDK, AutomationTask

maestro = BotMaestroSDK.from_sys_args()
execution = maestro.get_execution()


def main():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.FIREFOX

    bot.start_browser()

    try:
        bot.browse("https://quotes.toscrape.com/")
        bot.wait(2000)

        quotes = bot.find_elements(selector=".quote", by=By.CSS_SELECTOR)

        print(f"Total de citações encontradas: {len(quotes)}")

        for i, quote in enumerate(quotes, start=1):
            texto = quote.find_element(By.CSS_SELECTOR, ".text").text
            autor = quote.find_element(By.CSS_SELECTOR, ".author").text
            print(f"\n[{i}] {texto}\n    — {autor}")

        print("teste update")
        print("teste update")
        print("teste update")

        maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTask.Status.SUCCESS,
            message="Bot finalizado com sucesso.",
            total_items=len(quotes),
            processed_items=len(quotes),
        )

    except Exception as e:
        maestro.error(
            task_id=execution.task_id,
            exception=e,
            screenshot=bot.screenshot(),
            tags=["erro", "citacoes"],
        )
        maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTask.Status.FAILED,
            message=f"Erro durante a execução: {e}",
        )

    finally:
        bot.stop_browser()


if __name__ == "__main__":
    main()
