import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

# Title
ax.text(8, 8.5, 'Life Cycle Assessment Model - Milk Production',
        fontsize=22, fontweight='bold', ha='center')

# Define colors
box_color = '#1f7a8f'  # Teal blue similar to reference
text_color = 'white'
boundary_color = '#1f7a8f'

# Define positions for main lifecycle stages
stages = [
    {'x': 1.2, 'label': 'Raw Material\nExtraction', 'y': 5.5},
    {'x': 3.4, 'label': 'Material\nProcessing &\nManufacturing', 'y': 5.5},
    {'x': 5.8, 'label': 'Packaging &\nPreparation', 'y': 5.5},
    {'x': 8.2, 'label': 'Distribution &\nRetail Delivery', 'y': 5.5},
    {'x': 10.8, 'label': 'Use Phase', 'y': 5.5},
    {'x': 13.2, 'label': 'End-of-Life', 'y': 5.5},
]

# Draw system boundary box
boundary = FancyBboxPatch((0.6, 4.4), 13.2, 2.2,
                          boxstyle="round,pad=0.12",
                          edgecolor=boundary_color,
                          facecolor='none',
                          linewidth=3,
                          linestyle='-')
ax.add_patch(boundary)

# Add boundary label at top
ax.text(7.2, 6.8, 'System Boundary (Within Scope)',
        fontsize=12, ha='center', color=boundary_color, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=boundary_color, linewidth=2))

# Draw main stage boxes
box_width = 1.5
box_height = 0.9

for i, stage in enumerate(stages):
    # Create rounded rectangle
    fancy_box = FancyBboxPatch((stage['x'] - box_width/2, stage['y'] - box_height/2),
                              box_width, box_height,
                              boxstyle="round,pad=0.08",
                              edgecolor='none',
                              facecolor=box_color,
                              linewidth=2)
    ax.add_patch(fancy_box)

    # Add text inside box
    ax.text(stage['x'], stage['y'], stage['label'],
           fontsize=9.5, ha='center', va='center',
           color=text_color, fontweight='bold')

    # Add arrow to next stage (except last)
    if i < len(stages) - 1:
        arrow = FancyArrowPatch((stage['x'] + box_width/2 + 0.08, stage['y']),
                               (stages[i+1]['x'] - box_width/2 - 0.08, stages[i+1]['y']),
                               arrowstyle='->', mutation_scale=28,
                               linewidth=2.8, color=box_color)
        ax.add_patch(arrow)

# Add Energy Supply box below the manufacturing stage
energy_x = 3.4
energy_y = 3.2
fancy_box_energy = FancyBboxPatch((energy_x - 0.65, energy_y - 0.35), 1.3, 0.7,
                                 boxstyle="round,pad=0.08",
                                 edgecolor='none',
                                 facecolor=box_color,
                                 linewidth=2)
ax.add_patch(fancy_box_energy)
ax.text(energy_x, energy_y, 'Energy\nSupply',
       fontsize=9, ha='center', va='center',
       color=text_color, fontweight='bold')

# Arrow from energy to manufacturing
arrow_energy = FancyArrowPatch((energy_x, energy_y + 0.38), (energy_x, 5.05),
                              arrowstyle='->', mutation_scale=24,
                              linewidth=2.2, color=box_color, linestyle='--')
ax.add_patch(arrow_energy)

# Add inputs section on the left (outside boundary)
input_box_y = 2.5
ax.text(0.8, input_box_y + 1.2, 'Key Inputs', fontsize=11, fontweight='bold', ha='left',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0f0f0', edgecolor='#ccc', linewidth=1.5))
ax.text(0.8, input_box_y + 0.6, '• Raw Materials', fontsize=9, ha='left')
ax.text(0.8, input_box_y + 0.2, '  (Feed, Soybeans)', fontsize=8, ha='left', style='italic')
ax.text(0.8, input_box_y - 0.3, '• Water', fontsize=9, ha='left')
ax.text(0.8, input_box_y - 0.7, '• Energy', fontsize=9, ha='left')

# Add outputs section on the right (outside boundary)
output_box_y = 2.5
ax.text(15.2, output_box_y + 1.2, 'Key Outputs', fontsize=11, fontweight='bold', ha='right',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0f0f0', edgecolor='#ccc', linewidth=1.5))
ax.text(15.2, output_box_y + 0.6, '• GHG Emissions', fontsize=9, ha='right')
ax.text(15.2, output_box_y + 0.2, '• Water Footprint', fontsize=9, ha='right')
ax.text(15.2, output_box_y - 0.3, '• Land Use', fontsize=9, ha='right')
ax.text(15.2, output_box_y - 0.7, '• Waste', fontsize=9, ha='right')

# Add functional unit note at bottom
ax.text(8, 0.8, 'Functional Unit: One carton (1 liter) of refrigerated milk delivered to consumer',
       fontsize=10, ha='center', fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='#fffacd', edgecolor='#999', linewidth=1.5))

# Add note about comparison
ax.text(8, 0.15, 'System includes both dairy and soy milk production pathways',
       fontsize=9, ha='center', style='italic', color='#666')

plt.tight_layout()
plt.savefig(r'c:\עמרי\Shmags 2\projects\university\notes\LCA_System_Boundary_Milk.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Diagram saved: LCA_System_Boundary_Milk.png")
