from supabase import create_client

# Supabase credentials
SUPABASE_URL = "https://apmoxrzbjtntlzhslhga.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFwbW94cnpianRudGx6aHNsaGdhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzcxMjI3NjYsImV4cCI6MjA1MjY5ODc2Nn0.B1Zhvh_of0WVBpaSf8zVi5fSHCwbsc8soXoa3LG4hb4"

def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)
