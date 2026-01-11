#!/usr/bin/env python3
"""
Script untuk convert logo image ke Base64 dan update wifi_clone_login.h
Cara menggunakan:
    python convert_logo_to_base64.py path/to/your/logo.png
"""

import sys
import base64
from pathlib import Path

def convert_image_to_base64(image_path):
    """Convert image file ke Base64 string"""
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        base64_str = base64.b64encode(image_data).decode('utf-8')
        return base64_str
    except FileNotFoundError:
        print(f"❌ Error: File '{image_path}' tidak ditemukan!")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def get_mime_type(image_path):
    """Tentukan MIME type berdasarkan extension"""
    ext = Path(image_path).suffix.lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml',
        '.webp': 'image/webp'
    }
    return mime_types.get(ext, 'image/png')

def update_login_page(header_file, mime_type, base64_str):
    """Update wifi_clone_login.h dengan logo baru"""
    try:
        with open(header_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find dan replace logo data URI
        import re
        
        # Pattern untuk mencari data URI lama
        pattern = r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+'
        
        # Data URI baru
        new_data_uri = f'data:{mime_type};base64,{base64_str}'
        
        # Replace
        updated_content = re.sub(pattern, new_data_uri, content)
        
        # Write back
        with open(header_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
    except Exception as e:
        print(f"❌ Error updating header file: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("📸 Logo to Base64 Converter")
        print("=" * 50)
        print("Penggunaan:")
        print("  python convert_logo_to_base64.py <path_to_logo>")
        print()
        print("Contoh:")
        print("  python convert_logo_to_base64.py logo.png")
        print("  python convert_logo_to_base64.py C:\\Users\\Anda\\logo.jpg")
        print()
        print("Format yang didukung: PNG, JPG, JPEG, GIF, SVG, WEBP")
        return
    
    image_path = sys.argv[1]
    
    print(f"🔄 Mengkonversi: {image_path}")
    
    # Convert ke Base64
    base64_str = convert_image_to_base64(image_path)
    
    if base64_str is None:
        return
    
    mime_type = get_mime_type(image_path)
    
    print(f"✅ Konversi berhasil!")
    print(f"📊 Size: {len(base64_str):,} characters")
    print()
    
    # Tanyakan apakah ingin update file langsung
    header_file = Path(__file__).parent / 'include' / 'web' / 'wifi_clone_login.h'
    
    if header_file.exists():
        print(f"📁 Header file ditemukan: {header_file}")
        response = input("Apakah ingin update wifi_clone_login.h? (y/n): ").lower()
        
        if response == 'y':
            if update_login_page(str(header_file), mime_type, base64_str):
                print(f"✅ File berhasil diupdate!")
            else:
                print("❌ Gagal update file")
        else:
            print("\n📋 Base64 string (copy-paste ke file):")
            print("=" * 50)
            print(f"data:{mime_type};base64,{base64_str}")
            print("=" * 50)
    else:
        print(f"⚠️  Header file tidak ditemukan: {header_file}")
        print("\n📋 Base64 string (copy-paste ke file):")
        print("=" * 50)
        print(f"data:{mime_type};base64,{base64_str}")
        print("=" * 50)
    
    # Save to file untuk reference
    base64_file = Path(__file__).parent / 'logo_base64.txt'
    with open(base64_file, 'w') as f:
        f.write(f"Mime Type: {mime_type}\n")
        f.write(f"Size: {len(base64_str)} characters\n")
        f.write(f"Base64: {base64_str}\n")
    
    print(f"\n💾 Base64 juga disimpan ke: {base64_file}")

if __name__ == '__main__':
    main()
