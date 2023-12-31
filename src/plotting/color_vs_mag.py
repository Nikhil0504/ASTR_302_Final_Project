from astropy.table import Table
import matplotlib.pyplot as plt
from astropy import units as u

# ticks and tick labels
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['ytick.minor.visible'] = True

cat = Table.read('../../catalogs/master_catalog_f444w_astropy.cat', format='ascii', delimiter=' ')
zout = Table.read('../../catalogs/g165_444w_astropy.eazypy.zout.fits', format='fits')

z_phot = zout['z_phot']
mask = (z_phot == -1)

cat = cat[~mask]
zout = zout[~mask]

z_phot = zout['z_phot']


filters = ['F090W', 'F150W', 'F200W', 'F277W', 'F356W', 'F444W']

# convert mjy to AB mag
for filt in filters:
    cat[filt] = (cat[filt] * u.jansky * 1e-6).to(u.ABmag)

# plot color vs mag 3x3
fig, axes = plt.subplots(3, 3, figsize=(8, 8), sharex=True, sharey=True)
axes = axes.flatten()

# make a custom colormap based on redshift
mask_1 = (z_phot < 0.5)
mask_2 = ((z_phot >= 0.5) & (z_phot < 1.0))
mask_3 = ((z_phot >= 1.0) & (z_phot < 1.5))
mask_4 = ((z_phot >= 1.5) & (z_phot < 2.0))
mask_5 = ((z_phot >= 2.0) & (z_phot < 3))
mask_6 = (z_phot >= 3.)

colors = ['#5904BE', 'blue', '#1CFEFE', 'green', '#FA7228', 'red']

for i in range(6):
    mask = eval(f'mask_{i+1}')
    # axes[0].scatter(cat['F115W'][mask], cat['F090W'][mask] - cat['F115W'][mask], s=0.3, c=colors[i])
    # axes[1].scatter(cat['F150W'][mask], cat['F115W'][mask] - cat['F150W'][mask], s=0.3, c=colors[i])
    axes[2].scatter(cat['F200W'][mask], cat['F150W'][mask] - cat['F200W'][mask], s=0.3, c=colors[i])
    axes[3].scatter(cat['F277W'][mask], cat['F200W'][mask] - cat['F277W'][mask], s=0.3, c=colors[i])
    axes[4].scatter(cat['F444W'][mask], cat['F150W'][mask] - cat['F444W'][mask], s=0.3, c=colors[i])
    axes[5].scatter(cat['F444W'][mask], cat['F200W'][mask] - cat['F444W'][mask], s=0.3, c=colors[i])
    axes[6].scatter(cat['F356W'][mask], cat['F277W'][mask] - cat['F356W'][mask], s=0.3, c=colors[i])
    axes[7].scatter(cat['F444W'][mask], cat['F277W'][mask] - cat['F444W'][mask], s=0.3, c=colors[i])
    axes[8].scatter(cat['F444W'][mask], cat['F356W'][mask] - cat['F444W'][mask], s=0.3, c=colors[i])

# set x labels
axes[0].set_xlabel('F115W')
axes[1].set_xlabel('F150W')
axes[2].set_xlabel('F200W')
axes[3].set_xlabel('F277W')
axes[4].set_xlabel('F444W')
axes[5].set_xlabel('F444W')
axes[6].set_xlabel('F356W')
axes[7].set_xlabel('F444W')
axes[8].set_xlabel('F444W')

# set y labels
axes[0].set_ylabel('F090W - F115W')
axes[1].set_ylabel('F115W - F150W')
axes[2].set_ylabel('F150W - F200W')
axes[3].set_ylabel('F200W - F277W')
axes[4].set_ylabel('F150W - F444W')
axes[5].set_ylabel('F200W - F444W')
axes[6].set_ylabel('F277W - F356W')
axes[7].set_ylabel('F277W - F444W')
axes[8].set_ylabel('F356W - F444W')

axes[0].set_xlim(18, 30)
axes[0].set_ylim(-1, 2)

# add legend
axes[0].scatter([], [], s=10, c=colors[0], label='z < 0.5')
axes[1].scatter([], [], s=10, c=colors[1], label='0.5 < z < 1.0')
axes[2].scatter([], [], s=10, c=colors[2], label='1.0 < z < 1.5')
axes[3].scatter([], [], s=10, c=colors[3], label='1.5 < z < 2.0')
axes[4].scatter([], [], s=10, c=colors[4], label='2.0 < z < 3.0')
axes[5].scatter([], [], s=10, c=colors[5], label='z > 3.0')

axes[0].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=False)
axes[1].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=False)
axes[2].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=False)
axes[3].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=False)
axes[4].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=False)
axes[5].legend(loc='upper left', bbox_to_anchor=(0.0, 1.0), fontsize=8, frameon=False)


plt.savefig('../../plotting/color_vs_mag_f444w_astropy_g191.png', bbox_inches='tight', dpi=300)
plt.show()
