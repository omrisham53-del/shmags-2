# HW #2 - Functional Unit and System Boundary

## Question 1: Definition of Functional Unit and Its Criticality in LCA Studies

A functional unit is a standardized, measurable quantity that defines the service or function delivered by a product system. Rather than comparing products based solely on physical properties, the functional unit establishes a common reference point that enables fair comparison between different products serving the same purpose. In life cycle assessment, the functional unit is critical because it ensures systems are evaluated on the basis of equivalent utility.

The functional unit is essential in LCA studies for several reasons. First, it enables meaningful comparative assertions between competing products or systems. Without a clear functional unit, comparisons become arbitrary -- comparing one liter of milk to one kilogram of milk, for example, yields different results even though they represent the same product in different amounts. Second, the functional unit anchors all inventory data and impact calculations, ensuring environmental burdens are properly attributed to the service provided. Finally, it allows LCA results to be transparent and reproducible; future studies can use the same functional unit to validate or build upon previous findings.

## Question 2: Definition of System Boundary

A system boundary is the line separating processes included in a life cycle assessment from those deliberately excluded. It defines the scope of the analysis by specifying which lifecycle stages, and which activities or inputs within those stages, will be assessed for environmental impacts.

Establishing a clear system boundary is fundamental because it determines the completeness and relevance of the LCA. A narrow boundary can miss critical environmental hotspots; a boundary that is too broad becomes technically infeasible. The system boundary is defined both by lifecycle stages considered (from raw material extraction through end-of-life) and by the depth of analysis within each stage. Clear documentation is essential for interpreting results and for allowing others to assess the study's representativeness.

## Question 3: Analysis of the Chosen System -- Milk Production (Dairy vs. Soy)

### 3.1 Functional Unit

The functional unit for this analysis is: **one carton containing one liter of refrigerated milk, delivered to the consumer ready for consumption.**

This functional unit captures the essential service -- delivering a specific volume of drinkable milk in its typical commercial packaging. Specifying refrigerated milk is material because both dairy and soy milk are available commercially in refrigerated form, ensuring a fair comparison. This aligns with the standardized approach used in comprehensive LCA databases (Poore & Nemecek, 2018).

### 3.2 Lifecycle Stages and System Boundary

The system boundary follows a cradle-to-grave approach in accordance with ISO 14040/14044, encompassing six lifecycle stages.

**Stage 1: Raw Material Extraction**

For dairy milk, raw materials include cattle feed (alfalfa, ryegrass, corn, barley, soybean meal), water, and farm energy. The water footprint is substantial: approximately 628 liters of water per liter of milk produced, accounting for both drinking water and feed production (Poore & Nemecek, 2018).

For soy milk, raw materials consist of soybeans and water -- approximately 27-28 liters per liter of soy milk produced (Poore & Nemecek, 2018). This is roughly 22 times less water than dairy milk. Transportation of inputs (feed and soybeans) to processing facilities is a meaningful but sometimes overlooked contributor to emissions.

**Stage 2: Material Processing and Manufacturing**

For dairy milk, this stage involves pasteurization followed by cooling. Processing is energy-intensive due to continuous refrigeration requirements.

For soy milk, processing begins with soaking dried soybeans, then mechanical grinding into a slurry. The slurry is brought to a boil for 15-20 minutes to inactivate soybean trypsin inhibitor (STI) and sterilize the product (Cao et al., 2009). Insoluble residues are removed by straining and filtration, and defoaming agents (glycerin-based fatty acid esters) are added during boiling (Geburt et al., 2022).

**Stage 3: Assembly, Packaging, and Preparation**

Both systems use cartons composed of paper, polyethylene, and aluminum foil layers. Carton material production, filling, sealing, and labeling each require energy and contribute to the overall footprint.

**Stage 4: Distribution and Retail Delivery**

Both milk types require cold chain logistics from processing to retail: refrigerated trucks, distribution center storage, and retail refrigeration. The energy demand for maintaining cold temperatures is significant for both systems.

**Stage 5: Use Phase**

Both dairy and soy milk are stored in home refrigerators at similar temperatures, with a shelf life of approximately 2-3 weeks when properly refrigerated. Both spoil rapidly without refrigeration.

**Stage 6: End-of-Life**

Both milk cartons are recyclable. End-of-life processing involves sorting materials (paper, plastic, aluminum) for reuse or energy recovery, plus wastewater treatment of residual milk.

### 3.3 System Boundary Completeness and Hotspot Analysis

The primary environmental hotspot in this system is raw milk production. A systematic review of 84 dairy LCA studies published between 2018-2024 found that raw milk production consistently emerges as the largest environmental contributor across all impact categories, with fertilizer use, agricultural material production, and on-site emissions as the primary drivers for global warming potential, acidification, and eutrophication (González-García et al., 2025). For plant-based milk, hotspots shift to processing, packaging, and transportation rather than raw material production (Geburt et al., 2022).

One process included that could reasonably be excluded is retail refrigeration energy. Some LCA studies exclude this on the grounds that refrigeration systems serve multiple products simultaneously and attributing a specific share to any single product is imprecise. It is included here because both systems require identical cold-chain management at retail, making it material to the comparison. Its magnitude is likely small relative to the major production impacts, but inclusion improves completeness.

## Question 4: Functional Units for Non-Selected Cases

**Journey to university (Bus vs. Private EV Car):** One round-trip commute from Tel Aviv to Reichman University in Herzliya and back, representing a typical student journey to campus.

**Take-away coffee:** One 200-milliliter serving of coffee, delivered in a consumable form ready for drinking.

**Shopping bags:** One plastic shopping bag capable of carrying a standard grocery load.

**Producing electricity:** One megawatt-hour (MWh) of electricity delivered to the grid.

---

## References

Cao, X., Gu, Z., Zhang, Q., Zhang, S., & Wang, Z. (2009). Elimination of trypsin inhibitor activity and beany flavor in soy milk by consecutive blanching and ultrahigh-temperature (UHT) processing. *Journal of Agricultural and Food Chemistry*, 57(14), 6362-6368. https://doi.org/10.1021/jf801039h

Geburt, K., Albrecht, E. H., Pointke, M., Pawelzik, E., Gerken, M., & Traulsen, I. (2022). A comparative analysis of plant-based milk alternatives Part 2: Environmental impacts. *Sustainability*, 14(14), 8424. https://doi.org/10.3390/su14148424

González-García, S., Feijoo, G., & Moreira, M. T. (2025). Life cycle assessment applied to milk production and processing: An integrative systematic literature review. *Sustainability*, 17(4), 1615. https://doi.org/10.3390/su17041615

Poore, J., & Nemecek, T. (2018). Reducing food's environmental impacts through producers and consumers. *Science*, 360(6392), 987-992. https://doi.org/10.1126/science.aaq0216
