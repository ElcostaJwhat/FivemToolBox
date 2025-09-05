_H='Cleaner'
_G='DigitalEntitlements'
_F='~\\AppData\\Local'
_E='LOCALAPPDATA'
_D='end'
_C=None
_B=False
_A=True
import os,sys,psutil,socket,shutil,datetime,time,threading,ctypes,random,subprocess,customtkinter as ctk
from tkinter import messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
def is_admin():
	try:return ctypes.windll.shell32.IsUserAnAdmin()
	except:return _B
def run_as_admin():A=os.path.abspath(sys.argv[0]);ctypes.windll.shell32.ShellExecuteW(_C,'runas',sys.executable,A,_C,1);sys.exit()
def try_remove(file_path):
	A=file_path
	try:
		if os.path.exists(A):os.remove(A);return _A
	except(PermissionError,FileNotFoundError):pass
	return _B
def clean_folder(path,log_callback,progress_callback):
	D=log_callback;B=path
	if os.path.exists(B):
		E=os.listdir(B);F=len(E);C=0
		for G in E:
			A=os.path.join(B,G)
			if os.path.isdir(A):
				try:shutil.rmtree(A,ignore_errors=_A);D(A);C+=1
				except Exception as H:print(f"Err {A}: {H}")
			elif try_remove(A):D(A);C+=1
			progress_callback(C/F*100)
	else:print(f"Digi manquant{B} ")
def run_wmic_command(command):
	try:B=subprocess.check_output(command,shell=_A).decode().splitlines();A=[A.strip()for A in B if A.strip()];return'\n'.join(A)if A else'N/A'
	except subprocess.CalledProcessError as C:return str(C)
def get_machine_ids():A={};A['Disk Serial']=run_wmic_command('wmic diskdrive get serialnumber');A['System UUID']=run_wmic_command('wmic path win32_computersystemproduct get uuid');A['GPU Info']=run_wmic_command('wmic PATH Win32_VideoController GET Description,PNPDeviceID');A['CPU Serial']=run_wmic_command('wmic cpu get processorid');A['MAC Address']=run_wmic_command('wmic path Win32_NetworkAdapter where "PNPDeviceID like \'%%PCI%%\' AND NetConnectionStatus=2 AND AdapterTypeID=\'0\'" get MacAddress');return A
def cleanup(log_callback,progress_callback):
	C=log_callback;B=progress_callback
	try:
		E=os.getenv(_E,os.path.expanduser(_F));H=os.getenv('APPDATA',os.path.expanduser('~\\AppData\\Roaming'));F=[_G,'D3DSCache','cache','temp'];A=len(F);D=0
		for I in F:J=os.path.join(E,I);clean_folder(J,C,lambda progress:B(100*(D/A)+progress/A*100));D+=1
		K=os.path.join(E,'AMD');clean_folder(K,C,lambda progress:B(100*(D/A)+progress/A*100));G=os.path.join(E,'FiveM','FiveM.app');try_remove(G);C(G);L=os.path.join(H,'CitizenFX');clean_folder(L,C,lambda progress:B(100*(D/A)+progress/A*100));time.sleep(1);M=os.path.join(os.getenv('WINDIR','C:\\Windows'),'Temp');clean_folder(M,C,lambda progress:B(100*(D/A)+progress/A*100));messagebox.showinfo(_H,'Fivem est nettoyé pour le spoof');B(100);B(0)
	except Exception as N:messagebox.showerror('Error',str(N));B(0)
class FileDeletionHandler(FileSystemEventHandler):
	def __init__(A,existing_files,ui_update_callback):A.existing_files=existing_files;A.ui_update_callback=ui_update_callback
	def on_created(B,event):
		A=event
		if not A.is_directory:
			if A.src_path not in B.existing_files:
				if try_remove(A.src_path):B.ui_update_callback(A.src_path)
class FolderMonitor:
	def __init__(A,folder_path,ui_update_callback):A.folder_path=folder_path;A.observer=_C;A.thread=_C;A.running=_B;A.ui_update_callback=ui_update_callback
	def start_monitoring(A):
		if not A.running:B={os.path.join(A.folder_path,B)for B in os.listdir(A.folder_path)if os.path.isfile(os.path.join(A.folder_path,B))};C=FileDeletionHandler(B,A.ui_update_callback);A.observer=Observer();A.observer.schedule(C,A.folder_path,recursive=_B);A.observer.start();A.running=_A;print('surveillance en cours')
	def stop_monitoring(A):
		if A.running:A.observer.stop();A.observer.join();A.running=_B;print('surveillance arretée')
	def run(A):A.thread=threading.Thread(target=A.start_monitoring);A.thread.start()
	def stop(A):
		A.stop_monitoring()
		if A.thread:A.thread.join()
class App(ctk.CTk):
	def __init__(A,folder_monitor):E='both';D='background';C='Segoe';B='green';super().__init__();A.folder_monitor=folder_monitor;A.title('Fivem Tool By lejuan1');A.geometry('1200x800');ctk.set_appearance_mode('Dark');ctk.set_default_color_theme(B);F=ctk.CTkFont(family=C,size=20,weight='bold');G=ctk.CTkFont(family=C,size=14);H=ctk.CTkFont(family=C,size=12);A.label=ctk.CTkLabel(A,text='Fivem Toolbox',font=F);A.label.pack(pady=20);A.status=ctk.StringVar(value='Surveillance Stopée');A.status_label=ctk.CTkLabel(A,textvariable=A.status,font=G);A.status_label.pack(pady=10);A.main_frame=ctk.CTkFrame(A,fg_color=A.cget(D));A.main_frame.pack(pady=10,padx=20,fill=E,expand=_A);A.log_textbox=ctk.CTkTextbox(A.main_frame,width=600,height=400,corner_radius=10);A.log_textbox.pack(pady=10,padx=20,fill=E,expand=_A);A.progress_bar=ctk.CTkProgressBar(A.main_frame,width=100,progress_color=B);A.progress_bar.set(0);A.progress_bar.pack(padx=10,fill='x',expand=_A);A.toggle_button=ctk.CTkSwitch(A.main_frame,text='Activer Digifix',command=A.toggle_monitoring,fg_color='red',progress_color=B);A.toggle_button.pack(pady=10,padx=20);A.button_frame=ctk.CTkFrame(A.main_frame,fg_color=A.cget(D));A.button_frame.pack(pady=10,padx=20,fill='x');A.options=[(_H,A.start_cleanup),('Clear Logs',A.clear_logs),('Afficher les HWIDs',A.display_ids)];A.option_menu_var=ctk.StringVar(value=A.options[0][0]);A.option_menu=ctk.CTkOptionMenu(A.button_frame,variable=A.option_menu_var,values=[A[0]for A in A.options]);A.option_menu.pack(padx=10);A.confirm_button=ctk.CTkButton(A.button_frame,text='Confirmer',command=A.confirm_selection,corner_radius=10);A.confirm_button.pack(padx=10,pady=10)
	def confirm_selection(A):
		C=A.option_menu_var.get()
		for B in A.options:
			if B[0]==C:B[1]()
	def display_ids(A):C=get_machine_ids();B='\n\n'.join(f"{A}\n{B}"for(A,B)in C.items());A.log_textbox.delete('1.0',ctk.END);A.log_textbox.insert(ctk.END,B);A.save_hwids_to_file(B)
	def save_hwids_to_file(F,content):
		B=os.path.join(os.path.expanduser('~'),'Desktop');C=datetime.datetime.now();D=f"HWIDs_{C.strftime('%Y%m%d_%H%M%S')}.txt";A=os.path.join(B,D)
		with open(A,'w')as E:E.write(content)
		messagebox.showinfo('Fichier HWIDs',f"Le fichier HWIDs a été sauvegardé sur le bureau : {A}")
	def toggle_monitoring(A):
		if A.toggle_button.get()==1:A.folder_monitor.run();A.status.set('Status: Surveillance du dossier digitalentitlements en cours')
		else:A.folder_monitor.stop();A.status.set('Status: Surveillance Stopée')
	def start_cleanup(A):
		if is_admin():A.progress_bar.set(0);cleanup(A.update_ui_with_deletion,A.update_progress_bar)
		else:messagebox.showwarning('Admin Privileges','Execute le script en Admin');run_as_admin()
	def update_progress_bar(A,progress):A.progress_bar.set(progress)
	def update_ui_with_deletion(A,file_path):B=datetime.now().strftime('%H:%M:%S');C=os.path.basename(file_path);D=f"Nettoyé: {C} at {B}\n";A.log_textbox.insert(_D,D);A.log_textbox.see(_D)
	def clear_logs(A):A.log_textbox.delete('0.0',_D)
if __name__=='__main__':
	folder_to_monitor=os.path.join(os.getenv(_E,os.path.expanduser(_F)),_G)
	if not is_admin():run_as_admin()
	else:folder_monitor=FolderMonitor(folder_to_monitor,ui_update_callback=lambda x:app.update_ui_with_deletion(x));app=App(folder_monitor);app.mainloop()

