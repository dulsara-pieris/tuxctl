from rich.console import Console
import time

console = Console()

def verify_package():
    # Your real verification code goes here
    time.sleep(3)  # only for testing the spinner

with console.status("[cyan]Verifying package...[/cyan]", spinner="dots"):
    verify_package()

console.print("[green]✓ Verification complete[/green]")
