from rich.console import Console

console = Console()
console.print("\npra rodar comandos: [bold]make alvo[/bold]")

with open("./Makefile", "r") as file:
    for line in file.readlines():
        if line.find("##") >= 0:
            if line.find("@") >= 0:
                to_print = line.split("@")[-1].strip().capitalize()
                console.print(f"\n{to_print}", style="bold green")
            else:
                values = line.split("##")
                target = values[0]
                description = values[-1].strip().capitalize()
                target = target.split(":")[0].strip()
                console.print(f" - [bold]{target}:[/bold] {description}")
