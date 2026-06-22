import numpy as np
from scipy import signal
from scipy.ndimage import maximum_filter

def fingerprint_audio(audio_data, sr):

    f, t, Sxx = signal.spectrogram(
        audio_data,
        sr,
        nperseg=int(sr * 0.05)
    )

    spectrogram_db = 10 * np.log10(
        Sxx + 1e-10
    )

    local_max = (
        maximum_filter(
            spectrogram_db,
            size=15
        ) == spectrogram_db
    )

    threshold = np.percentile(
        spectrogram_db,
        90
    )

    peaks = (
        local_max &
        (spectrogram_db > threshold)
    )

    peak_freq_indices, peak_time_indices = np.where(peaks)

    peak_freqs = f[peak_freq_indices]
    peak_times = t[peak_time_indices]

    hashes = []

    for i in range(len(peak_times)):

        for j in range(1, 4):

            if i + j < len(peak_times):

                dt = peak_times[i+j] - peak_times[i]

                if 0 < dt < 5:

                    sig = (
                        int(peak_freqs[i]),
                        int(peak_freqs[i+j]),
                        round(dt,2)
                    )

                    hashes.append(
                        (
                            sig,
                            round(
                                peak_times[i],
                                2
                            )
                        )
                    )

    return (
        hashes,
        f,
        t,
        spectrogram_db,
        peak_freqs,
        peak_times
    )