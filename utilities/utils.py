import os, re
import datetime
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def reset_form():
    for key in st.session_state.keys():
        del st.session_state[key]
    customer_keys = ['customer_name', 'customer_mobile']
    for key in customer_keys:
        if key in st.session_state:
            del st.session_state[key]

    st.rerun()

def generate_enhanced_bill_image(title, customer_name, customer_mobile, total_price, discount, amount_paid, remaining_amount, file_path='enhanced_bill.png'):
    # Create a blank white image - Adjust the size if needed for your printer
    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)

    # Define text to be written
    now = datetime.datetime.now()
    current_date = now.strftime('%Y-%m-%d %H:%M:%S')
    modified_date = re.sub(r'[^a-zA-Z0-9]+', '_', current_date)

    file_path = f"{file_path}{modified_date}.png"
    img = Image.new('RGB', (576, 500), color='white')
    d = ImageDraw.Draw(img)

    # Prepare fonts - ensure the font files are in the same directory or provide full paths
    try:
        # Regular text
        font_regular = ImageFont.truetype("arial.ttf", 24)
        # Bold text
        font_bold = ImageFont.truetype("arialbd.ttf", 24)
    except IOError:
        # Fallback if Arial is not available
        font_regular = ImageFont.load_default()
        font_bold = ImageFont.load_default()

    items = [
        ("Date:", current_date),
        ("Customer Name:", customer_name),
        ("Customer Mobile:", customer_mobile),
        ("Total Price:", f"Rs {total_price:.2f}"),
        ("Discount:", f"Rs {discount:.2f}"),
        ("Amount Paid:", f"Rs {amount_paid:.2f}"),
        ("Remaining Amount:", f"Rs {remaining_amount:.2f}"),
    ]

    # Initial Y position
    y_pos = 30

    # Draw title centered
    _, _, title_width, title_height = d.textbbox((0, 0), title, font=font_bold)
    d.text(((576 - title_width) / 2, y_pos), title, fill="black", font=font_bold)
    y_pos += title_height + 20

    _, _, title_width, title_height = d.textbbox((0, 0), 'Sale Receipt', font=font_bold)
    d.text(((576 - title_width) / 2, y_pos), 'Sale Receipt', fill="black", font=font_bold)

    y_pos += title_height + 40

    # Draw items
    for label, value in items:
        # Label in bold
        d.text((10, y_pos), label, fill="black", font=font_bold)
        # Value in regular font
        value_x_pos = 300  # Adjust based on your content and receipt width
        d.text((value_x_pos, y_pos), value, fill="black", font=font_regular)
        y_pos += 40

    # Save the image
    img.save(file_path)
    print(f"Bill saved as {file_path}")
    return img
