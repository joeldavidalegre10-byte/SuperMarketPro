# model.py

class AppModel:
    """
    Maneja todos los datos de la aplicación y la lógica de negocio.
    Es completamente independiente de la interfaz de usuario.
    """
    def __init__(self):
        # Todos los datos de la aplicación viven aquí
        self.CASHIERS_DATA = [
            {"id": 1, "name": "Caja 01", "status": "open", "operator": "María González", "sales": 156},
            {"id": 2, "name": "Caja 02", "status": "open", "operator": "Juan Pérez", "sales": 143},
            {"id": 3, "name": "Caja 03", "status": "closed", "operator": None, "sales": 0},
            {"id": 4, "name": "Caja 04", "status": "open", "operator": "Ana Silva", "sales": 98},
            {"id": 5, "name": "Caja 05", "status": "closed", "operator": None, "sales": 0},
            {"id": 6, "name": "Caja 06", "status": "open", "operator": "Carlos Ruiz", "sales": 167},
            {"id": 7, "name": "Caja 07", "status": "maintenance", "operator": None, "sales": 0},
            {"id": 8, "name": "Caja 08", "status": "open", "operator": "Laura Díaz", "sales": 89},
            {"id": 9, "name": "Caja 09", "status": "open", "operator": "Roberto Sánchez", "sales": 134},
            {"id": 10, "name": "Caja 10", "status": "closed", "operator": None, "sales": 0},
            {"id": 11, "name": "Caja 11", "status": "open", "operator": "Patricia López", "sales": 112},
            {"id": 12, "name": "Caja 12", "status": "maintenance", "operator": None, "sales": 0},
            {"id": 13, "name": "Caja 13", "status": "open", "operator": "Diego Fernández", "sales": 78},
            {"id": 14, "name": "Caja 14", "status": "closed", "operator": None, "sales": 0},
            {"id": 15, "name": "Caja 15", "status": "maintenance", "operator": None, "sales": 0},
            {"id": 16, "name": "Caja 16", "status": "open", "operator": "Sofía Ramírez", "sales": 145},
            {"id": 17, "name": "Caja 17", "status": "open", "operator": "Miguel Torres", "sales": 91},
            {"id": 18, "name": "Caja 18", "status": "closed", "operator": None, "sales": 0},
            {"id": 19, "name": "Caja 19", "status": "maintenance", "operator": None, "sales": 0},
            {"id": 20, "name": "Caja 20", "status": "open", "operator": "Carmen Vargas", "sales": 156},
            {"id": 21, "name": "Caja 21", "status": "maintenance", "operator": None, "sales": 0},
            {"id": 22, "name": "Caja 22", "status": "closed", "operator": None, "sales": 0},
            {"id": 23, "name": "Caja 23", "status": "maintenance", "operator": None, "sales": 0},
            {"id": 24, "name": "Caja 24", "status": "open", "operator": "Fernando Castro", "sales": 102},
        ]
        self.MAINTENANCE_DATA = [
            {
                "id": 7, "name": "Caja 07",
                "issue": "Impresora de tickets no funciona",
                "details": "La impresora térmica no responde. Revisar cable de alimentación y conectividad USB.",
                "reported_by": "Ana Silva", "reported_date": "08/10/2025",
                "estimated_days": 2, "priority": "high"
            },
            {
                "id": 12, "name": "Caja 12",
                "issue": "Lector de código de barras intermitente",
                "details": "El escáner funciona de forma intermitente. Posible problema de cable o necesita reemplazo.",
                "reported_by": "Carlos Ruiz", "reported_date": "07/10/2025",
                "estimated_days": 1, "priority": "medium"
            },
            {
                "id": 15, "name": "Caja 15",
                "issue": "Cajón de dinero atascado",
                "details": "El mecanismo del cajón está trabado. Requiere limpieza y lubricación.",
                "reported_by": "María González", "reported_date": "06/10/2025",
                "estimated_days": 1, "priority": "high"
            },
            {
                "id": 19, "name": "Caja 19",
                "issue": "Pantalla táctil descalibrada",
                "details": "La pantalla no responde correctamente al tacto. Necesita recalibración o reemplazo.",
                "reported_by": "Juan Pérez", "reported_date": "09/10/2025",
                "estimated_days": 3, "priority": "medium"
            },
            {
                "id": 21, "name": "Caja 21",
                "issue": "Teclado numérico no funciona",
                "details": "Algunas teclas del teclado numérico no registran. Probablemente requiere reemplazo.",
                "reported_by": "Laura Díaz", "reported_date": "05/10/2025",
                "estimated_days": 2, "priority": "low"
            },
            {
                "id": 23, "name": "Caja 23",
                "issue": "Sistema operativo lento",
                "details": "El sistema tarda mucho en iniciar y procesar operaciones. Requiere optimización o actualización.",
                "reported_by": "Pedro Martínez", "reported_date": "04/10/2025",
                "estimated_days": 4, "priority": "low"
            },
        ]
        self.EARNINGS_DATA = {
            "today": {"total": 45230, "transactions": 152, "avg": 297},
            "week": [
                {"day": "Lun", "amount": 38420, "profit": 11526, "transactions": 145},
                {"day": "Mar", "amount": 42150, "profit": 12645, "transactions": 162},
                {"day": "Mié", "amount": 39870, "profit": 11961, "transactions": 138},
                {"day": "Jue", "amount": 44200, "profit": 13260, "transactions": 178},
                {"day": "Vie", "amount": 51340, "profit": 15402, "transactions": 195},
                {"day": "Sáb", "amount": 62580, "profit": 18774, "transactions": 234},
                {"day": "Dom", "amount": 35120, "profit": 10536, "transactions": 126},
            ],
            "month": {
                "total": 1250430,
                "profit": 375129,
                "growth": 18,
                "weeks": [
                    {"week": "Semana 1", "amount": 298450, "profit": 89535, "transactions": 1234},
                    {"week": "Semana 2", "amount": 315680, "profit": 94704, "transactions": 1301},
                    {"week": "Semana 3", "amount": 287920, "profit": 86376, "transactions": 1189},
                    {"week": "Semana 4", "amount": 348380, "profit": 104514, "transactions": 1432},
                ]
            },
        }
        self.INVENTORY_DATA = [
            {"id": 1, "name": "Laptop Dell XPS 15", "sku": "LAP-001", "stock": 45, "min_stock": 10, "price": 1299.99, "category": "Electrónica"},
            {"id": 2, "name": "Mouse Logitech MX Master", "sku": "ACC-002", "stock": 8, "min_stock": 15, "price": 99.99, "category": "Accesorios"},
            {"id": 3, "name": "Teclado Mecánico RGB", "sku": "ACC-003", "stock": 120, "min_stock": 20, "price": 149.99, "category": "Accesorios"},
            {"id": 4, "name": "Monitor LG 27 UHD", "sku": "MON-004", "stock": 67, "min_stock": 15, "price": 449.99, "category": "Monitores"},
            {"id": 5, "name": "Webcam Logitech C920", "sku": "ACC-005", "stock": 5, "min_stock": 10, "price": 79.99, "category": "Accesorios"},
        ]
        self.SALES_DATA = [
            {"id": 1, "cashier": "Caja 01", "amount": 1250.50, "items": 8, "time": "14:32", "payment": "Tarjeta", "customer": "Cliente Regular", "status": "completed"},
            {"id": 2, "cashier": "Caja 02", "amount": 856.00, "items": 5, "time": "14:28", "payment": "Efectivo", "customer": "Nuevo Cliente", "status": "completed"},
            {"id": 3, "cashier": "Caja 04", "amount": 2340.75, "items": 12, "time": "14:15", "payment": "Tarjeta", "customer": "Cliente VIP", "status": "completed"},
            {"id": 4, "cashier": "Caja 01", "amount": 456.20, "items": 3, "time": "14:05", "payment": "Efectivo", "customer": "Cliente Regular", "status": "completed"},
            {"id": 5, "cashier": "Caja 06", "amount": 1890.00, "items": 7, "time": "13:58", "payment": "Tarjeta", "customer": "Cliente Regular", "status": "pending"},
            {"id": 6, "cashier": "Caja 08", "amount": 345.75, "items": 4, "time": "13:45", "payment": "Efectivo", "customer": "Cliente Regular", "status": "refunded"},
            {"id": 7, "cashier": "Caja 02", "amount": 678.90, "items": 6, "time": "13:30", "payment": "Tarjeta", "customer": "Cliente VIP", "status": "completed"},
            {"id": 8, "cashier": "Caja 04", "amount": 234.50, "items": 2, "time": "13:20", "payment": "Efectivo", "customer": "Nuevo Cliente", "status": "pending"},
        ]

    def authenticate(self, username, password):
        """Lógica de autenticación simple. Devuelve True si no están vacíos."""
        return bool(username and password)

    def get_dashboard_stats(self):
        # CAMBIO: Se añaden todas las claves que necesita el nuevo dashboard.
        maintenance_count = len([c for c in self.CASHIERS_DATA if c['status'] == 'maintenance'])
        total_cashiers = len(self.CASHIERS_DATA) # AÑADIDO
        transactions_today = len(self.SALES_DATA)
        low_stock_count = len([p for p in self.INVENTORY_DATA if p['stock'] <= p['min_stock']]) # AÑADIDO
        month_growth = self.EARNINGS_DATA['month']['growth'] # AÑADIDO

        return {
            "maintenance_count": maintenance_count,
            "total_cashiers": total_cashiers, # AÑADIDO
            "transactions_today": transactions_today,
            "low_stock_count": low_stock_count, # AÑADIDO
            "month_growth": month_growth, # AÑADIDO
        }

    def get_cashiers(self, status_filter="all", search_query=""):
        """Filtra y devuelve las cajas."""
        data = self.CASHIERS_DATA
        if status_filter != "all":
            data = [c for c in data if c['status'] == status_filter]
        
        if search_query:
            query = search_query.lower()
            data = [
                c for c in data
                if query in c['name'].lower() or
                   (c['operator'] and query in c['operator'].lower())
            ]
        return data

    def get_cashier_stats(self):
        """Calcula y devuelve estadísticas de las cajas."""
        return {
            "open": len([c for c in self.CASHIERS_DATA if c['status'] == 'open']),
            "closed": len([c for c in self.CASHIERS_DATA if c['status'] == 'closed']),
            "maintenance": len([c for c in self.CASHIERS_DATA if c['status'] == 'maintenance']),
            "total_sales": sum(c['sales'] for c in self.CASHIERS_DATA),
            "total_cashiers": len(self.CASHIERS_DATA)
        }
    
    def get_maintenance_tasks(self, search_query=""):
        """Filtra y devuelve las tareas de mantenimiento."""
        data = self.MAINTENANCE_DATA
        if search_query:
            query = search_query.lower()
            data = [
                m for m in data
                if query in m['name'].lower() or
                   query in m['issue'].lower() or
                   query in m['details'].lower() or
                   query in m['reported_by'].lower()
            ]
        return data

    def get_maintenance_stats(self):
        total = len(self.MAINTENANCE_DATA)
        high_priority = len([m for m in self.MAINTENANCE_DATA if m['priority'] == 'high'])
        avg_days = round(sum(m['estimated_days'] for m in self.MAINTENANCE_DATA) / total) if total > 0 else 0
        return {"total": total, "high_priority": high_priority, "avg_days": avg_days}

    def get_earnings_data(self):
        return self.EARNINGS_DATA

    def get_inventory(self, stock_filter="all", search_query=""):
        """Filtra y devuelve los productos del inventario."""
        data = self.INVENTORY_DATA
        if stock_filter == "low": data = [p for p in data if p['stock'] <= p['min_stock']]
        elif stock_filter == "high": data = [p for p in data if p['stock'] > p['min_stock'] * 2]
        
        # El filtro 'normal' ya no es necesario
        
        if search_query:
            query = search_query.lower()
            data = [
                p for p in data
                if query in p['name'].lower() or
                   query in p['sku'].lower() or
                   query in p['category'].lower()
            ]
        return data

    def get_inventory_stats(self):
        total_products = len(self.INVENTORY_DATA)
        low_stock = len([p for p in self.INVENTORY_DATA if p['stock'] <= p['min_stock']])
        high_stock = len([p for p in self.INVENTORY_DATA if p['stock'] > p['min_stock'] * 2])
        total_value = sum(p['stock'] * p['price'] for p in self.INVENTORY_DATA)
        total_stock_units = sum(p['stock'] for p in self.INVENTORY_DATA)
        return {
            "total_products": total_products,
            "low_stock_count": low_stock,
            "high_stock_count": high_stock,
            "total_value": total_value,
            "total_stock_units": total_stock_units
        }

    def get_sales(self, status_filter="all", search_query=""):
        """Filtra y devuelve las ventas."""
        data = self.SALES_DATA
        if status_filter != "all":
            data = [s for s in self.SALES_DATA if s['status'] == status_filter]

        if search_query:
            query = search_query.lower()
            data = [
                s for s in data
                if query in str(s['id']) or
                   query in s['cashier'].lower() or
                   query in s['customer'].lower()
            ]
        return data

    def get_sales_stats(self):
        completed = [s for s in self.SALES_DATA if s['status'] == 'completed']
        pending = [s for s in self.SALES_DATA if s['status'] == 'pending']
        refunded = [s for s in self.SALES_DATA if s['status'] == 'refunded']
        return {
            "total_all": len(self.SALES_DATA),
            "total_completed": len(completed),
            "total_pending": len(pending),
            "total_refunded": len(refunded),
            "amount_completed": sum(s['amount'] for s in completed),
            "amount_pending": sum(s['amount'] for s in pending),
            "amount_refunded": sum(s['amount'] for s in refunded),
        }