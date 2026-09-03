import asyncio
from pathlib import Path
import edge_tts

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "en" / "audio"
OUT.mkdir(parents=True, exist_ok=True)

NARRATION = {
    1: "The Little Light That Came With Me. A story about first days, courage, and hope.",
    2: "The Little Light That Came With Me.",
    4: "The Little Light That Came With Me. A warm story for little hearts and brave souls.",
    5: "Some lights are not held in our hands. They shine inside our hearts.",
    6: "On the morning of her first day at preschool, Roshana opened her eyes and immediately knew that something was missing. The little light on her tummy usually shone like a star. But now it was only a tiny, dim dot. Roshana sighed. What if my light is afraid of preschool too?",
    8: "Roshana's mom fastened the straps of her backpack. It is okay to feel afraid, she said. When your heart beats fast, take one blink for a breath, and one blink for a step. One blink for a breath. One blink for a step.",
    10: "The path to preschool wound through the wet grass. Roshana walked behind Mom and softly repeated: one blink for a breath, one blink for a step. The sounds of laughter and play came closer, but Roshana's light was still small.",
    12: "By the door, a rabbit tossed a ball into the air. A squirrel slid down the slide. Miss Hedgehog, the kind teacher, bent down and said, Welcome, Roshana! But Roshana hid behind her backpack. She wanted to go home with Mom.",
    14: "At first, Roshana sat in the corner of the rug. Then she walked to the shelf of crayons and came back again. One blink for a breath, one blink for a step. A tear reached the tip of her nose. Just then, she heard a sob from the dark backpack room.",
    16: "A tiny beetle was lost among the big backpacks. My name is Poya, he said. I cannot find my shoes. It is so dark in here. Roshana was still afraid, but she knew how darkness felt. She took a breath and stepped forward. Her little light grew a little brighter.",
    18: "Roshana said, I am afraid too. Let us look together. The two friends walked slowly between the backpacks. One blink for a breath, one blink for a step. Roshana's light shone under a bench. There were two blue shoes!",
    20: "When Roshana and Poya returned to class, the children needed help building a little town. Roshana shone her light on the cardboard houses. Poya built a bridge, and Rabbit made a road. Roshana's light was warm and golden now. Not because she was no longer afraid, but because she had done something kind while afraid.",
    22: "That afternoon, when Mom arrived, Roshana ran to her like a little star. Mom asked, Did you bring your light from home? Roshana laughed. No! My light came from inside me. I only had to take one blink for a breath and one blink for a step.",
    24: "That night, Roshana did not turn off her light. She tucked it gently under the blanket, so her dreams could find their way home too.",
    25: "The end. One blink for a breath, one blink for a step.",
}

async def main():
    for page, text in NARRATION.items():
        voice = edge_tts.Communicate(text, "en-US-JennyNeural", rate="-7%", pitch="+4Hz", volume="+5%")
        await voice.save(str(OUT / f"page-{page:02d}.mp3"))

asyncio.run(main())
