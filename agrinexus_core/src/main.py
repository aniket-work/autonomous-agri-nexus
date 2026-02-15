import sys
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.markdown import Markdown
from rich.layout import Layout
from rich import print as rprint

from .sensors import SoilSensorNetwork
from .agents import CropConsultant

console = Console()

def main():
    # Header
    console.print(Panel.fit(
        "[bold green]AgriNexus-AI[/bold green]\n[italic]Autonomous Precision Agriculture Consultant[/italic]",
        border_style="green"
    ))

    # 1. Sensor Simulation
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task1 = progress.add_task("[cyan]Connecting to IoT Sensor Network...", total=100)
        
        # Simulate Network connection
        dummy_sensor = SoilSensorNetwork("corn")
        readings = dummy_sensor.read_sensors(zones=4)
        
        while not progress.finished:
            progress.update(task1, advance=5)
            time.sleep(0.05)
            
    # Display Sensor Data
    table = Table(title="Live Sensor Telemetry - Zone A (Corn)")
    table.add_column("Zone ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nitrogen (mg/kg)", justify="right")
    table.add_column("Moisture (%)", justify="right")
    table.add_column("Status", justify="center")

    for r in readings:
        status_color = "green" if r["status"] == "Optimal" else "red"
        table.add_row(
            str(r["zone_id"]), 
            f"{r['nitrogen']:.1f}", 
            f"{r['moisture']:.1f}", 
            f"[{status_color}]{r['status']}[/{status_color}]"
        )
    console.print(table)
    
    # Generate Heatmap (Silent)
    dummy_sensor.generate_heatmap(readings, filename="images/heatmap_generated.png")
    
    # 2. Agent Workflow
    agent = CropConsultant()
    
    # Phase 1: Diagnosis
    diagnosis = agent.analyze_field(readings)
    
    if diagnosis["anomalies"]:
        rprint(f"\n[bold red]⚠️  ALERT: {len(diagnosis['anomalies'])} Anomalies Detected[/bold red]")
        for a in diagnosis["anomalies"]:
            rprint(f"  - {a}")
    else:
        rprint("\n[bold green]✅ Field Status Optimal[/bold green]")
        return

    # Phase 2: Research
    with console.status("[bold blue]Agent Performing Live Research...", spinner="dots"):
        knowledge_base = agent.research_solutions(diagnosis["anomalies"], "corn")
        time.sleep(1.5) # UX Pause

    # Phase 3: Recommendations
    with console.status("[bold magenta]Synthesizing Action Plan...", spinner="earth"):
        rec = agent.generate_plan(diagnosis, knowledge_base)
        time.sleep(1.5) # UX Pause

    # Final Report
    rprint("\n")
    console.rule("[bold green]AGRINEXUS INTELLIGENCE REPORT[/bold green]")
    
    console.print(Panel(
        Markdown(rec.action_plan),
        title=f"strategic_advisory_{int(time.time())}.pdf",
        subtitle=f"Confidence: High | Sources: {len(rec.sources)}",
        border_style="green"
    ))
    
    rprint("\n[bold]Citations:[/bold]")
    for i, s in enumerate(rec.sources, 1):
        rprint(f" {i}. [italic]{s}[/italic]")

if __name__ == "__main__":
    main()
