import ehtim as eh
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo UVFITS
uvfits_file = 'path/to/your/file.uvfits'
obs = eh.obsdata.load_uvfits(uvfits_file)

# Extraer datos de visibilidad
u = obs.data['u']
v = obs.data['v']
amp = np.abs(obs.data['vis'])
phase = np.angle(obs.data['vis'])

# Graficar la amplitud de visibilidad y guardar en PNG
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(u, v, c=amp, cmap='viridis', s=1)
plt.colorbar(label='Amplitud')
plt.xlabel('u (lambda)')
plt.ylabel('v (lambda)')
plt.title('Amplitud de Visibilidad')

# Graficar la fase de visibilidad y guardar en PNG
plt.subplot(1, 2, 2)
plt.scatter(u, v, c=phase, cmap='twilight', s=1)
plt.colorbar(label='Fase (radianes)')
plt.xlabel('u (lambda)')
plt.ylabel('v (lambda)')
plt.title('Fase de Visibilidad')

# Ajustar el diseño y guardar la figura completa
plt.tight_layout()
plt.savefig('visibilidad_amplitud_y_fase.png', format='png', dpi=300)

# Mostrar las gráficas
plt.show()

