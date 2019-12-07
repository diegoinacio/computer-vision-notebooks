import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import librosa
import librosa.display
import numpy as np

def summary(x):
	if x.ndim == 1:
		SUM = ('\n{0:>10s}: {1:>15.4f}').format('min', np.amin(x))
		SUM += ('\n{0:>10s}: {1:>15.4f}').format('1st Quar', np.percentile(x, 25))
		SUM += ('\n{0:>10s}: {1:>15.4f}').format('median', np.median(x))
		SUM += ('\n{0:>10s}: {1:>15.4f}').format('mean', np.mean(x))
		SUM += ('\n{0:>10s}: {1:>15.4f}').format('3rd Quar', np.percentile(x, 75))
		SUM += ('\n{0:>10s}: {1:>15.4f}').format('max', np.amax(x))
		SUM += ('\n{0:>10s}: {1:>15.4f}').format('sigma', np.std(x))
	elif x.ndim == 2:
		E = x[:,0]
		D = x[:,1]
		SUM = ('{0:>%ss} {1:>%ss}' % (27, 15)).format('L', 'R')
		SUM += ('\n{0:>10s}: {1:>15.4f} {2:>15.4f}').format('min', np.amin(E), np.amin(D))
		SUM += ('\n{0:>10s}: {1:>15.4f} {2:>15.4f}').format('1st Quar', np.percentile(E, 25), np.percentile(D, 25))
		SUM += ('\n{0:>10s}: {1:>15.4f} {2:>15.4f}').format('median', np.median(E), np.median(D))
		SUM += ('\n{0:>10s}: {1:>15.4f} {2:>15.4f}').format('mean', np.mean(E), np.mean(D))
		SUM += ('\n{0:>10s}: {1:>15.4f} {2:>15.4f}').format('3rd Quar', np.percentile(E, 75), np.percentile(D, 75))
		SUM += ('\n{0:>10s}: {1:>15.4f} {2:>15.4f}').format('max', np.amax(E), np.amax(D))
		SUM += ('\n{0:>10s}: {1:>15.4f} {2:>15.4f}').format('sigma', np.std(E), np.std(D))
	else:
		raise ValueError('Invalid argument! It is not an audio..')
	print(SUM)

def audiovis(x, fs=44100, **kwargs):
	dx, dy = (1536, 512) if 'dims' not in kwargs else kwargs['dims']
	dpi = 72 if 'dpi' not in kwargs else kwargs['dpi']
	text = '' if 'text' not in kwargs else kwargs['text']

	samples = x.shape[0]
	time = samples/fs
	if 'time' not in kwargs:
		to, ti = [0, time]
	else:
		to, ti = kwargs['time'][[0, -1]]
	tmin, tmax = (to, ti) if 'tlim' not in kwargs else kwargs['tlim']
	t = np.linspace(to, ti, samples)

	if x.ndim == 1:
		print('audio mono')
		fig = plt.figure(figsize=(dx/dpi, dy/dpi))
		plt.plot(t, x)
		plt.xlim([tmin, tmax])
	elif x.ndim == 2:
		print('audio stereo')
		fig = plt.figure(figsize=(dx/dpi, 2*dy/dpi))
		plt.subplot(2, 1, 1)
		plt.plot(t, x[:, 0], color='#00ff88')
		plt.xlim([tmin, tmax])
		plt.subplot(2, 1, 2)
		plt.plot(t, x[:, 1], color='#0088ff')
		plt.xlim([tmin, tmax])
	else:
		raise ValueError('Invalid argument! It is not an audio..')
	plt.title(text)
	plt.show()

def spectrogram(x, fs=44100, **kwargs):
	dx, dy = (1536, 512) if 'dims' not in kwargs else kwargs['dims']
	dpi = 72 if 'dpi' not in kwargs else kwargs['dpi']
	fmin, fmax = [0, 8000] if 'flim' not in kwargs else kwargs['flim']
	text = '' if 'text' not in kwargs else kwargs['text']

	x = x.astype(np.float32)

	if x.ndim == 1:
		print('audio mono')
		fig = plt.figure(figsize=(dx/dpi, dy/dpi))
		X = np.abs(librosa.stft(x))
		X = librosa.amplitude_to_db(X, ref=np.max)
		librosa.display.specshow(X, sr=fs, y_axis='linear')
		plt.ylim([fmin, fmax])
		plt.colorbar(format='%+2.0f dB')
	elif x.ndim == 2:
		print('audio stereo')
		fig = plt.figure(figsize=(dx/dpi, 2*dy/dpi))
		plt.subplot(2, 1, 1)
		X = np.abs(librosa.stft(x[:, 0]))
		X = librosa.amplitude_to_db(X, ref=np.max)
		librosa.display.specshow(X, sr=fs, y_axis='linear')
		plt.ylim([fmin, fmax])
		plt.colorbar(format='%+2.0f dB')
		plt.subplot(2, 1, 2)
		X = np.abs(librosa.stft(x[:, 1]))
		X = librosa.amplitude_to_db(X, ref=np.max)
		librosa.display.specshow(X, sr=fs, y_axis='linear')
		plt.ylim([fmin, fmax])
		plt.colorbar(format='%+2.0f dB')
	else:
		raise ValueError('Invalid argument! It is not an audio..')
	plt.title(text)
	plt.show()