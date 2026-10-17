import os
import json
from PIL import Image

ASSETS_DIR = "assets"
OUT_DIR = os.path.join(ASSETS_DIR, "optimized")
os.makedirs(OUT_DIR, exist_ok=True)

# Catalog definition of showcase items (30 furniture pieces)
# Notice: logo.jpg, banner (777189214...), and timber photo (1790495923428) are EXCLUDED from gallery showcase
SHOWCASE_CATALOG = [
    {
        "id": "item-01",
        "file": "1790495440438.jpg.jpeg",
        "title": "Bespoke 4-Door Teak Wardrobe with Dressing Mirror",
        "category": "Wardrobes",
        "material": "Solid Teak & Natural Wood Polish",
        "description": "Floor-to-ceiling four-door wardrobe with grooved face detailing, integrated three-drawer dressing unit, and bevel-edge full-length mirror."
    },
    {
        "id": "item-02",
        "file": "1790495521516.jpg.jpeg",
        "title": "Artisan Slatted Accent Chair with Terracotta Bolster",
        "category": "Sofas & Seating",
        "material": "Seasoned Teak & Handloom Fabric",
        "description": "Hand-planed horizontal slat backrest with gentle ergonomic curve, fitted with high-density foam cushion and hand-stitched cylindrical bolster."
    },
    {
        "id": "item-03",
        "file": "1790495655377.jpg.jpeg",
        "title": "Handcrafted Studio Dining Chairs Suite",
        "category": "Dining",
        "material": "Solid Teak & Suede Upholstery",
        "description": "Workshop batch of six matching vertical-slat dining chairs finished in warm honey teak and upholstered in plush mocha suede."
    },
    {
        "id": "item-04",
        "file": "1790495660941.jpg.jpeg",
        "title": "Minimalist Teak Wardrobe with Integrated Vanity",
        "category": "Wardrobes",
        "material": "Teak Veneer & Brushed Steel Hardware",
        "description": "Modern multi-door wardrobe featuring full-length brushed steel handles, illuminated top pelmet, and a built-in dressing mirror ledge."
    },
    {
        "id": "item-05",
        "file": "1790495728758.jpg.jpeg",
        "title": "Teak Wood Slat Sofa with Storage Base",
        "category": "Sofas & Seating",
        "material": "Seasoned Teak Timber",
        "description": "Custom artisan sofa featuring curved hand-finished armrests, back slat support, deep seat framing, and concealed base storage."
    },
    {
        "id": "item-06",
        "file": "1790495791951.jpg.jpeg",
        "title": "Matte Slate Modular Wardrobe with Floating Vanity",
        "category": "Wardrobes",
        "material": "Anti-Fingerprint Matte Laminate & Teak Trim",
        "description": "Three-door contemporary slate grey wardrobe bordered in solid wood casing with a suspended floating vanity mirror and lockable drawers."
    },
    {
        "id": "item-07",
        "file": "1790495975706.jpg.jpeg",
        "title": "L-Shaped Gloss Cream Modular Kitchen & Glass Display",
        "category": "Kitchens",
        "material": "Gloss Acrylic & Black Profile Handles",
        "description": "Full modular kitchen layout featuring handleless overhead lofts, black granite countertop, corner ergonomics, and a tall tinted glass crockery cabinet."
    },
    {
        "id": "item-08",
        "file": "1790496145559.jpg.jpeg",
        "title": "Modern Cooking Counter with Built-in Hob & Pan Drawers",
        "category": "Kitchens",
        "material": "High-Gloss Acrylic & Soft-Close Channels",
        "description": "Precision cooktop counter with seamlessly recessed multi-burner gas hob, soft-closing tandem pan drawers, and matching overhead cabinets."
    },
    {
        "id": "item-09",
        "file": "1790496266825.jpg.jpeg",
        "title": "Contemporary Modular Kitchen Full Perspective",
        "category": "Kitchens",
        "material": "Acrylic Shutter Panels & Polished Granite",
        "description": "Spacious L-shaped kitchen layout showcasing seamless backsplash tiling, floor cabinetry, deep corner carousel space, and ambient lighting."
    },
    {
        "id": "item-10",
        "file": "1790496338473.jpg.jpeg",
        "title": "Full-Height Champagne Gloss Wardrobe with Top Lofts",
        "category": "Wardrobes",
        "material": "High-Gloss Champagne Acrylic & Matte Black Pulls",
        "description": "Four-door floor-to-ceiling modular wardrobe suite with dedicated upper loft storage and 1200mm matte black vertical handles."
    },
    {
        "id": "item-11",
        "file": "1790496500474 (1).jpg.jpeg",
        "title": "Nordic Blue & White Modular Kitchen with Corner Sink",
        "category": "Kitchens",
        "material": "Moisture-Resistant Marine Ply & Matte Blue Laminate",
        "description": "Airy custom kitchen designed for natural window light, featuring corner double-bowl sink, fluted glass crockery cabinet, and overhead lofts."
    },
    {
        "id": "item-12",
        "file": "1790496564042.jpg.jpeg",
        "title": "Space-Saving Round Dining Table with 4 Nesting Chairs",
        "category": "Dining",
        "material": "Solid Teak & Tempered Black Glass",
        "description": "Clever space-saving circular dining table with four curved slat-back chairs designed to tuck completely flush beneath the perimeter."
    },
    {
        "id": "item-13",
        "file": "1790496663240.jpg.jpeg",
        "title": "L-Shaped Teak Sectional Sofa & Cabriole Coffee Table",
        "category": "Sofas & Seating",
        "material": "Solid Teak Wood & Rust Orange Upholstery",
        "description": "Expansive corner sectional living room sofa in rich honey teak wood paired with a hand-carved floral cabriole-leg coffee table."
    },
    {
        "id": "item-14",
        "file": "1790496739030.jpg.jpeg",
        "title": "Walnut Open Bookshelf & Media Console with X-Brace",
        "category": "TV Units & Partitions",
        "material": "American Walnut Finish & Solid Wood Framing",
        "description": "Architectural asymmetrical bookshelf and media console featuring cross-braced center display alcove and modular cubbies."
    },
    {
        "id": "item-15",
        "file": "1790496822199.jpg.jpeg",
        "title": "Dual-Tone Teak & Slate Wardrobe with Vanity Bench",
        "category": "Wardrobes",
        "material": "Natural Teak & Matte Slate Grey Laminate",
        "description": "Three-door wardrobe bordered by solid teak frame and crown, topped with high lofts and a cushioned low vanity dressing station."
    },
    {
        "id": "item-16",
        "file": "1790506776206.jpg.jpeg",
        "title": "Coffered Teak Main Entrance Door with Fluted Glass",
        "category": "Doors & Windows",
        "material": "100% Solid Seasoned Teak",
        "description": "Grand two-leaf main entrance door crafted with nine coffered raised-field wood panels, brushed steel vertical handle, and horizontal fluted privacy glass."
    },
    {
        "id": "item-17",
        "file": "1790506845672.jpg.jpeg",
        "title": "Warm Cream Bedside Nightstand with Brushed Brass Knobs",
        "category": "Beds & Bedroom",
        "material": "Lacquered Hardwood & Solid Brass Accents",
        "description": "Custom bedside nightstand with upper pull drawer and lower swing cabinet, designed to pair seamlessly with upholstered bedroom suites."
    },
    {
        "id": "item-18",
        "file": "1790506884483.jpg.jpeg",
        "title": "3-Panel Architectural Window with Frosted Geometric Art Glass",
        "category": "Doors & Windows",
        "material": "Teak Wood Frame & Toughened Art Glass",
        "description": "Triple-panel external window frame built from teak with security grills and decorative etched geometric glass lights."
    },
    {
        "id": "item-19",
        "file": "1790506933257.jpg.jpeg",
        "title": "X-Frame Handcrafted Dining Bench with Textured Cushion",
        "category": "Dining",
        "material": "Teak Wood & High-Durability Woven Fabric",
        "description": "Sturdy architectural dining bench with cross-leg timber trestle base and a deeply padded charcoal grey upholstered seat."
    },
    {
        "id": "item-20",
        "file": "1790506973624.jpg.jpeg",
        "title": "Sculptural Curved Teak Barstools in Sky Blue Leatherette",
        "category": "Sofas & Seating",
        "material": "Teak Hardwood & Marine Blue Leatherette",
        "description": "Pair of ergonomic counter-height barstools with curved bentwood backrests, double foot stretchers, and tailored blue cushions."
    },
    {
        "id": "item-21",
        "file": "1790507013071.jpg.jpeg",
        "title": "Contemporary 3-Seater Sofa with Fluted Timber Arms",
        "category": "Sofas & Seating",
        "material": "Dark Walnut Finish & Grey Heather Weave",
        "description": "Three-seater living room sofa with wide boxed timber armrests featuring horizontal flute carvings and supportive lumbar pillows."
    },
    {
        "id": "item-22",
        "file": "1790507090416.jpg.jpeg",
        "title": "Designer Dual-Wood Door with Asymmetrical Glass Insets",
        "category": "Doors & Windows",
        "material": "Teak Outer Frame & Walnut Center Panel",
        "description": "Statement entry door combining light honey teak borders with dark walnut core paneling, accented by asymmetric frosted glass slits."
    },
    {
        "id": "item-23",
        "file": "1790507134383.jpg.jpeg",
        "title": "Curved High-Back Teak Dining Chair with Cabriole Legs",
        "category": "Dining",
        "material": "Solid Teak & Natural Linen Fabric",
        "description": "Traditional high-back dining chair featuring ten curved lumbar vertical splats, cabriole front legs, and neutral linen seat cushion."
    },
    {
        "id": "item-24",
        "file": "1790507286793.jpg.jpeg",
        "title": "Teak Wood Interior Door with Sweeping CNC Arc Grooves",
        "category": "Doors & Windows",
        "material": "Seasoned Teak Wood & Antique Brass Lever",
        "description": "Interior room door with subtle continuous circular arc routing celebrating the natural grain patterns of teak."
    },
    {
        "id": "item-25",
        "file": "1790507330037.jpg.jpeg",
        "title": "Full-Wall Modular TV Unit & Display Partition Grid",
        "category": "TV Units & Partitions",
        "material": "Teak Wood Veneer & Smoked Glass Base Cabinets",
        "description": "Symmetrical full-wall entertainment unit with central TV mounting panel, surrounding open lattice shelving grid, and dark base drawers."
    },
    {
        "id": "item-26",
        "file": "1790507405276.jpg.jpeg",
        "title": "Heritage Teak Daybed / Diwan with Lion-Paw Carved Legs",
        "category": "Beds & Bedroom",
        "material": "100% Raw Seasoned Teak",
        "description": "Traditional Indian diwan daybed built from raw solid teak wood, featuring a slatted recline back and hand-carved lion-paw claw feet."
    },
    {
        "id": "item-27",
        "file": "1790507453367.jpg.jpeg",
        "title": "5-Tier Pyramid Corner Display Etagere Stand",
        "category": "TV Units & Partitions",
        "material": "Solid Teak with Tapered Stile Frame",
        "description": "Five-tier freestanding corner what-not shelf with sweeping outward-curved base legs and graduated shelves for artifacts and planters."
    },
    {
        "id": "item-28",
        "file": "1790507499478.jpg.jpeg",
        "title": "Architectural Timber Partition Arch with Low Book Ledge",
        "category": "TV Units & Partitions",
        "material": "Hardwood Veneer & Walnut Polish",
        "description": "Space-defining room divider portal bridging the living room and modular kitchen, featuring integrated low storage shelves."
    },
    {
        "id": "item-29",
        "file": "1790507674542.jpg.jpeg",
        "title": "Hand-Carved Heritage Pooja / Temple Door with Floral Frame",
        "category": "Doors & Windows",
        "material": "A-Grade Solid Teak & Traditional Carving",
        "description": "Exquisite temple room entrance door featuring intricately hand-carved floral vine architrave, nine floral-boss panels, and solid brass pull ring."
    },
    {
        "id": "item-30",
        "file": "1790507733748.jpg.jpeg",
        "title": "Solid Teak Slat Garden / Verandah Bench & Low Table",
        "category": "Sofas & Seating",
        "material": "All-Weather Solid Teak Timber",
        "description": "Two-piece patio/verandah furniture set with horizontal slat two-seater bench and matching recessed-frame cabriole coffee table."
    }
]

print(f"Total showcase items configured: {len(SHOWCASE_CATALOG)}")

processed_gallery = []

for item in SHOWCASE_CATALOG:
    src_file = os.path.join(ASSETS_DIR, item["file"])
    if not os.path.exists(src_file):
        print(f"Warning: {src_file} does not exist!")
        continue
    
    # Base slug
    base_name = os.path.splitext(os.path.basename(item["file"]))[0].replace(" (1)", "_1").replace(".", "_")
    
    with Image.open(src_file) as img:
        img_rgb = img.convert("RGB")
        orig_w, orig_h = img.size
        aspect_ratio = round(orig_h / orig_w, 4)
        
        # 1. 480w (Mobile)
        w480 = min(480, orig_w)
        h480 = int(round(orig_h * (w480 / orig_w)))
        out480_path = os.path.join(OUT_DIR, f"{base_name}_480w.webp")
        img_rgb.resize((w480, h480), Image.Resampling.LANCZOS).save(out480_path, "WEBP", quality=85)
        
        # 2. 800w (Tablet / Grid)
        w800 = min(800, orig_w)
        h800 = int(round(orig_h * (w800 / orig_w)))
        out800_path = os.path.join(OUT_DIR, f"{base_name}_800w.webp")
        img_rgb.resize((w800, h800), Image.Resampling.LANCZOS).save(out800_path, "WEBP", quality=88)
        
        # 3. 1200w (Lightbox)
        w1200 = min(1200, orig_w)
        h1200 = int(round(orig_h * (w1200 / orig_w)))
        out1200_path = os.path.join(OUT_DIR, f"{base_name}_1200w.webp")
        img_rgb.resize((w1200, h1200), Image.Resampling.LANCZOS).save(out1200_path, "WEBP", quality=90)
        
        processed_gallery.append({
            "id": item["id"],
            "title": item["title"],
            "category": item["category"],
            "material": item["material"],
            "description": item["description"],
            "orig_file": item["file"],
            "width": orig_w,
            "height": orig_h,
            "aspect_ratio": aspect_ratio,
            "src": f"assets/optimized/{base_name}_800w.webp",
            "thumb": f"assets/optimized/{base_name}_480w.webp",
            "full": f"assets/optimized/{base_name}_1200w.webp",
            "srcset": f"assets/optimized/{base_name}_480w.webp 480w, assets/optimized/{base_name}_800w.webp 800w, assets/optimized/{base_name}_1200w.webp 1200w",
            "sizes": "(max-width: 640px) 100vw, (max-width: 1024px) 50vw, (max-width: 1440px) 33vw, 25vw"
        })

# Process Hero Banner (777189214...)
hero_src = os.path.join(ASSETS_DIR, "777189214_1772764893764912_6432006908235877688_n.webp")
if os.path.exists(hero_src):
    with Image.open(hero_src) as img:
        img_rgb = img.convert("RGB")
        ow, oh = img.size
        # 800w, 1400w, 2048w
        for w in [800, 1400, 2048]:
            tw = min(w, ow)
            th = int(round(oh * (tw / ow)))
            img_rgb.resize((tw, th), Image.Resampling.LANCZOS).save(os.path.join(OUT_DIR, f"hero_{tw}w.webp"), "WEBP", quality=90)
    print("Hero banner optimized successfully.")

# Process Timber photo for About/Workshop (1790495923428.jpg.jpeg)
timber_src = os.path.join(ASSETS_DIR, "1790495923428.jpg.jpeg")
if os.path.exists(timber_src):
    with Image.open(timber_src) as img:
        img_rgb = img.convert("RGB")
        ow, oh = img.size
        for w in [600, 1000]:
            tw = min(w, ow)
            th = int(round(oh * (tw / ow)))
            img_rgb.resize((tw, th), Image.Resampling.LANCZOS).save(os.path.join(OUT_DIR, f"timber_{tw}w.webp"), "WEBP", quality=90)
    print("Timber photo optimized successfully.")

# Generate Favicons from logo-transparent.png
logo_trans_src = os.path.join(ASSETS_DIR, "logo-transparent.png")
if os.path.exists(logo_trans_src):
    with Image.open(logo_trans_src) as logo_img:
        logo_img.resize((180, 180), Image.Resampling.LANCZOS).save(os.path.join(ASSETS_DIR, "apple-touch-icon.png"), "PNG")
        logo_img.resize((32, 32), Image.Resampling.LANCZOS).save(os.path.join(ASSETS_DIR, "favicon-32x32.png"), "PNG")
        logo_img.resize((16, 16), Image.Resampling.LANCZOS).save(os.path.join(ASSETS_DIR, "favicon-16x16.png"), "PNG")
        # Multi-size ICO
        logo_img.save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print("Favicons generated successfully.")

# Save catalog JSON
catalog_path = os.path.join("js", "gallery-data.json")
os.makedirs("js", exist_ok=True)
with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(processed_gallery, f, indent=2)

print(f"Gallery data written to {catalog_path} with {len(processed_gallery)} items.")
