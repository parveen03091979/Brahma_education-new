# PURCHASE - PENDING MODE - SECURE
pur={
    "invoice_no":inv,
    "access_key":access_key,
    "date":str(datetime.datetime.now()),
    "name":name,"email":email,"phone":phone,
    "whatsapp":whatsapp,"city":city,
    "course":c.get('topic',''),
    "price":c.get('price',999),
    "course_id":c.get('id',''),
    "utr":utr,
    "upi_id":MY_UPI_ID,
    "status":"PENDING",  # NEW - PENDING
    "payment_verified":False
}
purchases.append(pur); save_purchases(purchases)
st.warning("⏳ Payment Verification Pending - Admin 24 Hour me check karke Approve karega")
st.info(f"Your Request ID: {inv} - UTR: {utr} - Admin check ke baad hi Access Key kaam karega")
st.code(f"REQUEST ID: {inv} - Isse status check kar sakte ho")