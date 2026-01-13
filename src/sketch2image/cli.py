import click
from .models import generate_image

@click.command()
@click.argument("sketch_path", type=click.Path(exists=True))
@click.argument("output_path", type=click.Path())
@click.option("--model", default="nano-banana", help="The AI model to use for image generation.")
def main(sketch_path, output_path, model):
    """
    Converts a sketch to a full-color image using an AI model.
    """
    click.echo(f"🎨 Converting sketch: {sketch_path}")
    click.echo(f"🖼️ Saving to: {output_path}")
    click.echo(f"🤖 Using model: {model}")

    # from .models import generate_image
    generate_image(sketch_path, output_path, model)

    click.echo("✅ Image generated successfully!")

if __name__ == "__main__":
    main()
