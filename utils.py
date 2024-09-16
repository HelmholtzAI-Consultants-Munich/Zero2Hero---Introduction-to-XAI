############################################################
##### Imports
############################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.cluster import hierarchy

############################################################
##### Utility Functions
############################################################


def plot_distributions(dataset, ncols):

    nrows = int(np.ceil(len(dataset.columns) / ncols))

    plt.figure(figsize=(ncols * 4.5, nrows * 4.5))
    plt.subplots_adjust(top=0.95, hspace=0.8, wspace=0.8)
    plt.suptitle("Distribution of features")

    for n, feature in enumerate(dataset.columns):
        # add a new subplot iteratively
        ax = plt.subplot(nrows, ncols, n + 1)
        if dataset[feature].nunique() < 5 or isinstance(dataset[feature].dtype, pd.CategoricalDtype):
            sns.countplot(
                data=dataset,
                x=feature,
                hue=feature,
                palette="Blues_r",
                ax=ax,
            )
            # ax.legend(bbox_to_anchor=(1, 1), loc=2)
        else:
            sns.histplot(
                data=dataset,
                x=feature,
                bins=30,
                ax=ax,
                color="#3470a3",
            )

    plt.tight_layout(rect=[0, 0, 1, 0.95])


def plot_permutation_feature_importance(result, data, title, top_n=None, figsize=(7, 5)):
    # Sort the features by importance mean
    perm_sorted_idx = result.importances_mean.argsort()[::-1]

    # If top_n is provided, limit the selection to top_n features
    if top_n:
        perm_sorted_idx = perm_sorted_idx[:top_n]

    # Prepare the data for Seaborn's boxplot (convert to long format)
    feature_importances = result.importances[perm_sorted_idx].T
    df = pd.DataFrame(feature_importances, columns=data.columns[perm_sorted_idx])
    df_long = df.melt(var_name="Feature", value_name="Importance")

    # Create the figure and plot
    fig, ax = plt.subplots(figsize=figsize)
    sns.boxplot(
        data=df_long, x="Importance", y="Feature", ax=ax, flierprops=dict(marker=".", alpha=0.5, markersize=2)
    )

    # Set title and layout
    ax.set_title(title)
    fig.tight_layout()
    plt.show()


def plot_permutation_feature_importance_train_vs_test(
    result_train, data_train, result_test, data_test, title, figsize=(10, 4)
):
    perm_sorted_idx = result_train.importances_mean.argsort()
    perm_indices = np.arange(0, len(result_train.importances_mean)) + 0.5

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    fig.suptitle(title)
    ax1.barh(
        perm_indices,
        result_train.importances_mean[perm_sorted_idx],
        height=0.7,
        color="#3470a3",  # color = 'cornflowerblue'
    )
    ax1.set_yticks(perm_indices)
    ax1.set_yticklabels(data_train.columns[perm_sorted_idx])
    ax1.set_ylim((0, len(result_train.importances_mean)))

    perm_sorted_idx = result_test.importances_mean.argsort()
    perm_indices = np.arange(0, len(result_test.importances_mean)) + 0.5

    ax2.barh(
        perm_indices,
        result_test.importances_mean[perm_sorted_idx],
        height=0.7,
        color="#3470a3",  # color = 'cornflowerblue'
    )
    ax2.set_yticks(perm_indices)
    ax2.set_yticklabels(data_test.columns[perm_sorted_idx])
    ax2.set_ylim((0, len(result_test.importances_mean)))

    fig.tight_layout()
    plt.show()


def plot_impurity_feature_importance(importance, names, title, top_n=None, figsize=(5, 4), fontsize=8):
    # Create arrays from feature importance and feature names
    feature_importance = np.array(importance)
    feature_names = np.array(names)

    # Create a DataFrame using a Dictionary
    data = {"feature_names": feature_names, "feature_importance": feature_importance}
    fi_df = pd.DataFrame(data)

    # Sort the DataFrame in order decreasing feature importance
    fi_df.sort_values(by=["feature_importance"], ascending=False, inplace=True)

    if top_n:
        fi_df = fi_df.iloc[:top_n]

    # Define size of bar plot
    fig, ax = plt.subplots(figsize=figsize)
    # Plot Searborn bar chart
    sns.barplot(x=fi_df["feature_importance"], y=fi_df["feature_names"], color="#3470a3")
    # Add chart labels
    plt.title(title)
    plt.xlabel("Feature Importance (mean decrease in impurity)")
    plt.ylabel("Feature Names")
    ax.set_yticklabels(ax.get_yticks(), fontsize=fontsize)


def plot_explanation(explanation):
    explanation_df = pd.DataFrame({k: v for k, v in explanation.items() if k != "importances"}).sort_values(
        by="importances_mean", ascending=True
    )

    f, ax = plt.subplots(1, 1, figsize=(9, 7))
    explanation_df.plot(kind="barh", ax=ax)
    plt.title("Permutation importances")
    plt.axvline(x=0, color=".5")
    plt.subplots_adjust(left=0.3)

    if "feature" in explanation_df:
        _ = ax.set_yticklabels(explanation_df["feature"])


def plot_correlation_matrix(data, figsize=(5, 5), annot=True, labelsize=10, shrink=1):
    corr = data.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    np.fill_diagonal(mask, False)

    f, ax = plt.subplots(figsize=figsize)
    ax.tick_params(axis="both", which="major", labelsize=labelsize)
    sns.heatmap(
        round(corr, 2),
        mask=mask,
        cmap=sns.diverging_palette(220, 10, as_cmap=True),
        cbar_kws={"shrink": shrink},
        square=True,
        ax=ax,
        annot=annot,
    )


def plot_dendrogram(linked, feature_names, figsize=(5, 5), leaf_font_size=10):

    # Create a figure
    plt.figure(figsize=figsize)

    # Plot the dendrogram
    dendrogram = hierarchy.dendrogram(
        linked,
        orientation="top",  # 'top', 'bottom', 'left', or 'right'
        distance_sort="descending",  # 'ascending' or 'descending'
        show_leaf_counts=True,  # Show the number of observations in each cluster
        leaf_rotation=90,  # Rotation of leaf labels
        leaf_font_size=leaf_font_size,  # Font size of leaf labels
        show_contracted=True,  # Show contracted leaves
        labels=feature_names,
    )

    # Add title and labels
    plt.title("Dendrogram")
    plt.xlabel("Feature")
    plt.ylabel("Distance")

    # Show the plot
    plt.show()
