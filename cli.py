# import argparse
# from rich import print
# from rich.panel import Panel
# from rich.table import Table

# from bot.client import get_client
# from bot.orders import place_order
# from bot.validators import validate_input
# from bot.logging_config import setup_logger


# def main():
#     setup_logger()

#     parser = argparse.ArgumentParser()

#     parser.add_argument("--symbol", required=True)
#     parser.add_argument("--side", required=True)
#     parser.add_argument("--type", required=True)
#     parser.add_argument("--quantity", required=True)
#     parser.add_argument("--price", required=False)

#     args = parser.parse_args()

#     try:
#         validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

#         print(Panel.fit("🚀 Placing Order...", style="bold blue"))

#         client = get_client()

#         order = place_order(
#             client,
#             args.symbol,
#             args.side,
#             args.type,
#             args.quantity,
#             args.price
#         )

#         table = Table(title="📊 Order Result")

#         table.add_column("Field", style="cyan")
#         table.add_column("Value", style="green")

#         table.add_row("Symbol", args.symbol)
#         table.add_row("Side", args.side)
#         table.add_row("Type", args.type)
#         table.add_row("Order ID", str(order.get("orderId")))
#         table.add_row("Status", order.get("status"))
#         table.add_row("Executed Qty", str(order.get("executedQty")))
#         table.add_row("Avg Price", str(order.get("avgPrice", "N/A")))

#         print(table)
#         print("[bold green]✅ Order placed successfully[/bold green]")

#     except Exception as e:
#         print(f"[bold red]❌ Error: {str(e)}[/bold red]")


# if __name__ == "__main__":
#     main()




from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger


def main():
    setup_logger()

    print(Panel.fit("🚀 Binance Trading Bot", style="bold blue"))

    # 🎯 Interactive Inputs
    symbol = Prompt.ask("Enter Symbol", default="BTCUSDT")

    side = Prompt.ask(
        "Select Side",
        choices=["BUY", "SELL"],
        default="BUY"
    )

    order_type = Prompt.ask(
        "Select Order Type",
        choices=["MARKET", "LIMIT"],
        default="MARKET"
    )

    quantity = Prompt.ask("Enter Quantity", default="0.01")

    price = None
    if order_type == "LIMIT":
        price = Prompt.ask("Enter Price")

    try:
        validate_input(symbol, side, order_type, quantity, price)

        print(Panel.fit("📡 Sending Order...", style="yellow"))

        client = get_client()

        order = place_order(
            client,
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        # 📊 Beautiful Table Output
        table = Table(title="📊 Order Result", show_lines=True)

        table.add_column("Field", style="cyan", justify="center")
        table.add_column("Value", style="green", justify="center")

        table.add_row("Symbol", symbol)
        table.add_row("Side", side)
        table.add_row("Type", order_type)
        table.add_row("Order ID", str(order.get("orderId")))
        table.add_row("Status", order.get("status"))
        table.add_row("Executed Qty", str(order.get("executedQty")))
        table.add_row("Avg Price", str(order.get("avgPrice", "N/A")))

        print(table)

        print(Panel.fit("✅ Order placed successfully!", style="bold green"))

    except Exception as e:
        print(Panel.fit(f"❌ Error: {str(e)}", style="bold red"))


if __name__ == "__main__":
    main()