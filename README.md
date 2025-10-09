# realistic_kraljic
#Overview

The Kraljic Portfolio Analysis is a strategic procurement tool that helps organizations classify their products or materials based on two key factors — Supply Risk and Profit Impact.
This project aims to analyze supplier and product data to determine the best sourcing strategy for each product category.
By using this framework, companies can optimize their supply chain, minimize risk, and maximize profitability.  

#Problem Statement

Organizations often face challenges in managing suppliers and products with varying levels of risk, cost, and strategic importance.
Without a structured approach, procurement teams may fail to identify which products require long-term partnerships or which can be sourced competitively.
This project solves that issue by applying the Kraljic Matrix model to classify items into:
Leverage Items
Strategic Items
Non-critical Items
Bottleneck Items

#Dataset
The dataset contains product-level information relevant to supplier management and risk evaluation.
It includes the following key columns:

Column Name	Description
Product_ID	Unique identifier for each product
Product_Name	Name or description of the product
Supplier_Region	Geographical region of the supplier
Lead_Time_Days	Average time taken for delivery
Order_Volume_Units	Quantity ordered per cycle
Cost_per_Unit	Cost of one unit of the product
Supply_Risk_Score	Numeric score representing supply chain risk (1–10)
Profit_Impact_Score	Score indicating profit contribution (1–10)
Environmental_Impact	Impact score based on sustainability
Single_Source_Risk	Binary or score showing dependency on one supplier
Kraljic_Category	Final classification according to the matri

#Tools & Technologies
This project uses a combination of data analytics and visualization tools to perform portfolio analysis:
Python – for data manipulation and analysis
Pandas & NumPy – for handling and processing data
Plotly & Matplotlib – for visualizing risk vs. profit matrix
Streamlit – for building an interactive dashboard
Scikit-learn – for scaling, clustering, or risk modeling (if applied)
Jupyter Notebook – for exploratory data analysis (EDA)

#Key Insights
Products with high Supply Risk and high Profit Impact fall into the Strategic category — requiring partnership and careful management.
Leverage items offer high profit but low risk — suitable for competitive sourcing.
Bottleneck items pose risk due to supply constraints despite low profit impact — need contingency planning.
Non-critical items are low in both risk and impact — can be standardized and automated for efficiency.
The Supplier Region analysis helps identify high-risk areas or regions with longer lead times.
Cost analysis highlights potential savings through better supplier negotiation for high-volume products.

#Conclusion
The Kraljic Portfolio Analysis provides a structured, data-driven way to improve supply chain strategy.
By segmenting products based on risk and profit impact, organizations can:
Focus efforts on strategic partnerships,
Reduce supply chain vulnerabilities,
Optimize cost efficiency, and
