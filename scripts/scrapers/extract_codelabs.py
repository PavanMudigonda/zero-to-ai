import asyncio
import pandas as pd
from playwright.async_api import async_playwright

async def scrape_codelabs():
    url = "https://codelabs.developers.google.com/?category=aiandmachinelearning"
    all_codelabs = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print(f"Navigating to {url}")
        
        await page.goto(url)
        # Wait for the initial load just to be safe
        await page.wait_for_timeout(5000)

        print("Scraping all loaded cards from the DOM...")
        
        # Extract all cards present in the DOM
        cards = await page.locator('.devsite-card-wrapper').all()
        print(f"Found {len(cards)} card elements in DOM.")
        
        for card in cards:
            title = await card.get_attribute('displaytitle')
            href = await card.get_attribute('url')
            category = await card.get_attribute('category')
            products = await card.get_attribute('display-tag-product')
            duration = await card.get_attribute('formattedduration')
            
            # Explicitly filter only cards that have the AI & ML category
            if title and href and category and 'aiandmachinelearning' in category:
                # Construct full URL if relative
                full_url = f"https://codelabs.developers.google.com{href}" if href.startswith("/") else href
                
                # Determine a primary high-level category based on title or products
                primary_category = "Other AI/ML"
                title_lower = title.lower()
                products_lower = products.lower() if products else ""
                
                if "gemini" in title_lower or "generative" in title_lower or "llm" in title_lower:
                    primary_category = "Generative AI & Gemini"
                elif "vertex" in title_lower or "vertex ai" in products_lower:
                    primary_category = "Vertex AI"
                elif "tensorflow" in title_lower or "tensorflow" in products_lower or "keras" in title_lower:
                    primary_category = "TensorFlow & Keras"
                elif "bigquery" in title_lower or "bqml" in title_lower:
                    primary_category = "BigQuery ML"
                elif "vision" in title_lower or "language" in title_lower or "speech" in title_lower or "translation" in title_lower or "api" in title_lower:
                    primary_category = "Pre-trained ML APIs"
                elif "spark" in title_lower or "dataproc" in title_lower or "dataflow" in title_lower:
                    primary_category = "Data Processing & Spark ML"
                
                all_codelabs.append({
                    "Sub-Category": primary_category,
                    "Title": title.strip(),
                    "Products": products if products else "None",
                    "Duration": duration if duration else "Unknown",
                    "Link": full_url
                })
                
        await browser.close()
        
    return all_codelabs

def main():
    codelabs_data = asyncio.run(scrape_codelabs())
    
    if codelabs_data:
        df = pd.DataFrame(codelabs_data)
        output_file = "ai_ml_codelabs.xlsx"
        df.to_excel(output_file, index=False)
        print(f"Successfully extracted {len(codelabs_data)} codelabs and saved to {output_file}")
    else:
        print("No codelabs found.")

if __name__ == "__main__":
    main()
