import pandas as pd

df = pd.read_csv("fake_claims.csv")

# --- Cleaning ---
print("Rows before cleaning:", len(df))

df = df.drop_duplicates()
df["ICD10_Code"] = df["ICD10_Code"].str.strip().str.upper()
df["Payer"] = df["Payer"].str.strip().replace({"tawuniya": "Tawuniya"})

print("Rows after cleaning:", len(df))
print("\nMissing values per column:")
print(df.isna().sum())

# --- Analysis ---
rejected = df[df["Status"] == "Rejected"]

print("\nRejected claims by payer:")
print(rejected["Payer"].value_counts())
df["Is_Rejected"] = df["Status"] == "Rejected"

rate = df.groupby("Payer")["Is_Rejected"].mean() * 100

print("\nRejection rate by payer (%):")
print(rate.round(1).sort_values(ascending=False))
summary = pd.DataFrame({
    "Total_Claims": df.groupby("Payer").size(),
    "Rejected_Claims": df.groupby("Payer")["Is_Rejected"].sum(),
    "Rejection_Rate_%": (df.groupby("Payer")["Is_Rejected"].mean() * 100).round(1),
}).sort_values("Rejection_Rate_%", ascending=False)

reasons = rejected["Rejection_Reason"].value_counts().reset_index()
reasons.columns = ["Rejection_Reason", "Count"]

with pd.ExcelWriter("rejection_report.xlsx") as writer:
    summary.to_excel(writer, sheet_name="By_Payer")
    reasons.to_excel(writer, sheet_name="Reasons", index=False)

print("Report saved: rejection_report.xlsx")
print("\nClaim with missing amount:")
print(df[df["Claim_Amount_SAR"].isna()])

loss = rejected.groupby("Rejection_Reason")["Claim_Amount_SAR"].sum()

print("\nRejected amount by reason (SAR):")
print(loss.round(0).sort_values(ascending=False))
import matplotlib.pyplot as plt

loss.sort_values().plot(kind="barh", color="#1F4E78")
plt.title("Rejected amount by reason (SAR)")
plt.xlabel("SAR")
plt.tight_layout()
plt.savefig("rejected_amount_by_reason.png", dpi=150)

print("Chart saved: rejected_amount_by_reason.png")
df.to_csv("claims_clean.csv", index=False, encoding="utf-8-sig")
print("Clean data saved: claims_clean.csv")