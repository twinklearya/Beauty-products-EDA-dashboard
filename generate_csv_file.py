import pandas as pd

# Sample data for beauty products
data = {
    'product_name': [
        'Luminous Silk Foundation', 'Rouge Lipstick', 'Glow Primer',
        'Smooth Sunscreen', 'Hydrating Serum', 'Matte Blush',
        'Volume Mascara', 'Nourishing Conditioner', 'Radiant Eye Cream', 'Daily Moisturizer'
    ],
    'brand': [
        'Giorgio Armani', 'Dior', 'Becca', 'Neutrogena', 'The Ordinary',
        'NARS', 'Maybelline', 'Aveda', 'Olay', 'Cetaphil'
    ],
    'price': [64, 38, 36, 12, 7, 30, 8, 24, 28, 10],
    'rating': [4.7, 4.5, 4.3, 4.2, 4.6, 4.4, 4.1, 4.3, 4.5, 4.4],
    'reviews': [1243, 875, 322, 412, 965, 543, 125, 234, 875, 654],
    'category': [
        'Foundation', 'Lipstick', 'Primer', 'Sunscreen', 'Serum', 
        'Blush', 'Mascara', 'Conditioner', 'Eye Cream', 'Moisturizer'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('beauty_products.csv', index=False)

print("CSV file 'beauty_products.csv' created successfully.")
