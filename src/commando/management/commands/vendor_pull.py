from django.core.management.base import BaseCommand
from typing import Any
import statichelpers
from django.conf import settings

STATICFILES_VENDOR_DIRS = getattr(settings, 'STATICFILES_VENDOR_DIRS')


  

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
    "flowbite.min.js.map": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js.map",
  
}



class Command(BaseCommand):
    
    def handle(self, *args:any, **options:any):
        self.stdout.write("django static files are downloading...")
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIRS / name
            dl_success = statichelpers.download_static_to_local(url, out_path)
            
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f"failed to Download {url}"))
                
        if set(completed_urls) ==set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS("Successfully updated all vendor static files"))
        
        else:
            self.stdout.write(self.style.ERROR('some files are not updated'))
            
        