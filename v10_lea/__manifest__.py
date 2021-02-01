{
    'name' : 'PT Lea Sanent',
    'version' : '10',    
    'category': 'Custom',    
    'author' :'Alfius Samuel Sutopo',        
    'depends' : ['product','stock', 'sale', 'account', 'base', 'report','point_of_sale', 'purchase','stock_account', 'sales_team'],
    'data': [                    
        'views/lea_view.xml',
        'views/stock_inventory_view.xml',
        'views/groups.xml',
        'views/menu.xml',
        'views/report_invoice.xml',
        'views/report_stockpicking.xml',
        'views/report_type_pdf.xml',
        'views/lea_target_store_view.xml',
        'views/lea_target_consignment_view.xml',
        'views/lea_target_salesman_view.xml',
        'views/stock_replenishment_view.xml',
        'views/sales_temporary_view.xml',

        'views/stock_report_template.xml',
        'views/report_pos_sale_outlet_view.xml',
        'views/report_summary_sales_performance_class_view.xml',
        'views/report_summary_sales_performance_channel_view.xml',
        'views/report_summary_sales_performance_comparison_view.xml',

        'wizard/create_job_picking_view.xml',
        'wizard/create_packing_list_view.xml',
        'wizard/stock_report_view.xml',
        'wizard/change_customer_type_view.xml',
        'wizard/create_coli_wizard.xml',
        'wizard/update_product_column_view.xml',
        'wizard/create_replenishment_view.xml',
        'wizard/merge_journal_view.xml',
        'wizard/pos_sale_detail_view.xml',
        'wizard/create_invoice_view.xml',
        'wizard/wizard_summary_sales_performance_class_view.xml',
        'wizard/wizard_summary_sales_performance_channel_view.xml',
        'wizard/wizard_summary_sales_performance_comparison_view.xml',

        'wizard/confirm_sale_order_view.xml',
        'wizard/dashboard_sales_view.xml',
        'data/ir_sequence.xml',   
        'v10_lea_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
