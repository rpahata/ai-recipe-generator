from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()

# ✅ FLAN-T5 model (stable + free)
model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


class RecipeRequest(BaseModel):
    ingredients: str


def build_prompt(ingredients: str):
    return f"""
You are a professional chef.

Create a SIMPLE, REAL cooking recipe using ONLY these ingredients:
{ingredients}

Rules:
- Do NOT add unnecessary ingredients
- Only salt, oil, water allowed
- Must be realistic
- No stories, no explanation

Format exactly:

Recipe Name:
Ingredients:
Steps:
"""


@app.post("/generate-recipe")
def generate_recipe(req: RecipeRequest):
    prompt = build_prompt(req.ingredients)

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=False
    )

    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"recipe": recipe}