

REPEAT_CUSTOMERS_QUERY = '''
SELECT 
    c.full_name,
    si.invoice_number,
    c.ltv,
    c.aov,
    c.no_of_bills,
    c.last_purchase_amount,
    c.last_purchase_store_id,
    c.last_purchase_bill_date,
    c.last_purchase_amount
FROM customers c
LEFT JOIN (
    SELECT DISTINCT ON (customer_id) 
        invoice_number, customer_id, created_at
    FROM sales_invoices
    ORDER BY customer_id, created_at DESC
) si ON si.customer_id = c.id
WHERE 
    c.last_purchase_bill_date IN (
        CURRENT_DATE - INTERVAL '27 days', 
        CURRENT_DATE - INTERVAL '57 days',
        CURRENT_DATE - INTERVAL '87 days'
    );
'''

LOST_CUSTOMERS_QUERY = '''
SELECT 
    c.full_name,
    si.invoice_number,
    c.ltv,
    c.aov,
    c.no_of_bills,
    c.last_purchase_amount,
    c.last_purchase_store_id,
    c.last_purchase_bill_date,
    c.last_purchase_amount
FROM customers c
LEFT JOIN (
    SELECT DISTINCT ON (customer_id) 
        invoice_number, customer_id, created_at
    FROM sales_invoices
    ORDER BY customer_id, created_at DESC
) si ON si.customer_id = c.id
WHERE 
    c.last_purchase_bill_date IN (
        CURRENT_DATE - INTERVAL '27 days', 
        CURRENT_DATE - INTERVAL '57 days'
    );
'''

NEW_CUSTOMERS_QUERY = '''
SELECT 
    c.full_name,
    si.invoice_number,
    c.ltv,
    c.aov,
    c.no_of_bills,
    c.last_purchase_amount,
    c.last_purchase_store_id,
    c.last_purchase_bill_date,
    c.last_purchase_amount
FROM customers c
LEFT JOIN (
    SELECT DISTINCT ON (customer_id) 
        invoice_number, customer_id, created_at
    FROM sales_invoices
    ORDER BY customer_id, created_at DESC
) si ON si.customer_id = c.id
WHERE 
    c.last_purchase_bill_date IN (
        CURRENT_DATE - INTERVAL '102 days', 
        CURRENT_DATE - INTERVAL '132 days'
    );
'''